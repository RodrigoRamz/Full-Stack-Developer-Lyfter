import json
import os

from transaction import Transaction

DEFAULT_CATEGORIES = [
    "Food",
    "Services",
    "Transportation",
    "Housing & Rent",
    "Debt",
    "Savings",
    "Health",
    "Entertainment",
    "Sports",
    "Salary", 
]

class FinancialManager:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.transactions = [] #Objects Transaction List
        self.categories = DEFAULT_CATEGORIES.copy() #Capital Case strings list

        self.load_data()

    def add_category(self, category_name: str) -> bool:
        """
        Add a new category:
        - Clean spaces
        - Avoid Duplicates
        - Save Capital Case
        - ErrorMessage is not displayed if the category exists      
        """
        category_name = category_name.strip()
        if not category_name:
            return False
            
        normalized = category_name.lower()

        for existing in self.categories:
            if existing.lower() == normalized:
                return False
            
        category_name_cap = category_name.capitalize()
        self.categories.append(category_name_cap)
        self.save_data()
        return True

    def add_transaction(self, title: str, amount: float, transaction_type: str, date: str, category: str):
        """
        Creates and saves a new transaction.
        Logic:
        - Adjust the amount as per its transaction type
        - Category Validation
        - Creates the Transaction
        - Save in JSON
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be a numeric value")
        
        transaction_type = transaction_type.strip().upper()

        if transaction_type not in ("INCOME", "EXPENDITURE"):
            raise ValueError("Invalid transaction type")

        if transaction_type == "INCOME":
            amount = abs(amount) # positive numbers
        else: 
            amount = -abs(amount) #negative numbers

        normalized = category.strip().lower()
        canonical_category = None

        for existing in self.categories:
            if existing.lower() == normalized:
                canonical_category = existing
                break

        if canonical_category is None:
            raise ValueError("Category does not exist")
        
        t = Transaction(title=title,
                        amount=amount,
                        transaction_type=transaction_type,
                        date=date,
                        category=canonical_category
        )
        
        self.transactions.append(t)
        self.save_data()
        

    def calculate_balance(self) -> float:
        """Sum all the transactions amounts"""
        return sum(t.amount for t in self.transactions)

    def save_data(self):
        """
        Write the JSON file with the next format:
        {
            "transactions": [...],
            "categories': [...], 
        }
        """
        data = {
            "transactions": [t.to_dict() for t in self.transactions],
            "categories": self.categories,
        }

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)    

    def load_data(self):
        """
        Load the data from the JSON file.
        If does not exists -> Empty Lists.
        Converts the dictionaries into Transaction objects
        """
        if not os.path.exists(self.filepath): #no file yet -> start clean
            self.transactions = []
            self.categories = DEFAULT_CATEGORIES.copy()
            return
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            self.transactions = []
            self.categories = DEFAULT_CATEGORIES.copy()
            return
        
        transactions_data = data.get("transactions", [])
        categories_data = data.get("categories", DEFAULT_CATEGORIES.copy())

        self.transactions = []
        for t_data in transactions_data:
            t = Transaction(
                title=t_data["title"],
                amount=t_data["amount"],
                transaction_type=t_data["transaction_type"],
                date=t_data["date"],
                category=t_data["category"],
            )
            self.transactions.append(t)
        self.categories = categories_data

    def to_table_values(self):
        """
        Converts all the transactions in lists to the GUI Table.
        Depends on the Transaction.to_row() method.
        """
        return [t.to_row() for t in self.transactions]
        