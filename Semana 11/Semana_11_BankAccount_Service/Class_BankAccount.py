class BankAccount:
    def __init__(self, balance: float = 0.0):
        """Constructor: Starting Bank Account Balance"""
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        """Add the amount of money of your deposit"""
        if amount <= 0:
            raise ValueError("Deposit should be higher than $0")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Bank Account Withdraw."""
        if amount <= 0:
            raise ValueError("Withdraw must be higher than $0")
        if amount > self.balance:
            raise ValueError("Insufficient Founds")
        self.balance -= amount

    def __repr__(self) -> str:
        return f"BankAccount(balance={self.balance: .2f})"
    

class SavingsAccount(BankAccount):
    def __init__(self, balance: float = 0.0, min_balance: float = 0.0):
        """Constructor: Start Balance and Minimum Balance"""
        super().__init__(balance)
        self.min_balance = float(min_balance)

    def withdraw(self, amount: float) -> None:
        """Considers the minimum balance"""
        if self.balance - amount < self.min_balance:
            raise ValueError("Withdraw Denied due to Minimum Balance allowed")
        return super().withdraw(amount)
    
    def __repr__(self) -> str:
        return (f"SavingsAccount(balance={self.balance: .2f}, "
                f"min_balance={self.min_balance: .2f})")