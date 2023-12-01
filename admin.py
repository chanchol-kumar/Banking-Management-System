from user import User
# Admin Class
class Admin:
    bank_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

# Create Account Method
    @classmethod
    def create_account(cls, name, initial_balance=0, loan_limit=0):
        user = User(name, initial_balance, loan_limit)
        cls.bank_balance += initial_balance
        return user

# Check Bank Balance Method
    @classmethod
    def check_bank_balance(cls):
        return cls.bank_balance
    
# Check Total Loan Amount Method
    @classmethod
    def check_total_loan_amount(cls):
        return cls.total_loan_amount

# Toggle Loan Feature Method 
    @classmethod
    def toggle_loan_feature(cls, enable):
        cls.loan_feature_enabled = enable
        if enable:
            print("Loan feature is now enabled.")
        else:
            print("Loan feature is now disabled.")
