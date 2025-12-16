class Transaction:
    def __init__(self, title: str, amount: float, transaction_type: str, date: str, category: str):
        """
        Here we have the validations:
        - Title is not Empty
        - Amount are numbers
        - Date is noy Empty
        - Transaction_type INCOME / EXPENDITURE
        """
        title_clean = (title or "").strip()
        if not title_clean:
            raise ValueError("Transaction title cannot be empty")
        
        self.title = title_clean
        
        try:
            self.amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Amount must be a numeric value")
        
        self.transaction_type = transaction_type
        if transaction_type not in ("INCOME", "EXPENDITURE"):
            raise ValueError("Invalid transaction type")
        
        self.date = date
        if not date:
            raise ValueError("Date cannot be empty")
        self.category = category
        if not category:
            raise ValueError("Category cannot be empty")

    def to_dict(self):
        """Converts the transaction into a dictionary in the JSON file."""
        return {
            "transaction_type": self.transaction_type,
            "category": self.category,
            "title": self.title,
            "amount": self.amount,
            "date": self.date,
            
        }

    def to_row(self):
        """Converts the transaction into a list to utilize it in sg.Table."""
        return [
            self.transaction_type,
            self.category,
            self.title,
            self.amount,
            self.date,
        ]
    