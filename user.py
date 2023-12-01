# User Class
class User:
    def __init__(self, name, initial_balance=0, loan_limit=0):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []
        self.loan_limit = loan_limit

# Deposit Method
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

# Withdraw Method
    def withdraw(self, amount, admin_balance):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount} ৳")
        else:
            if amount > self.balance + admin_balance:
                print("The bank is bankrupt. Unable to withdraw.")
            else:
                print("Insufficient funds. Unable to withdraw.")

# Transfer Method
    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred {amount} ৳ to {recipient.name}")
        else:
            print("Insufficient funds. Unable to transfer.")

# Check Balance Method
    def check_balance(self):
        return self.balance

# Get Loan Method
    def get_loan(self):
        if self.balance * 2 <= self.loan_limit:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            self.transaction_history.append(f"Got a loan of {loan_amount} ৳")
            return loan_amount
        else:
            print("Loan limit exceeded. Unable to get a loan.")
            return 0

# Transaction History Method
    def check_transaction_history(self):
        return self.transaction_history
