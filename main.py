from user import User
from admin import Admin

# Main Program
admin = Admin()

person1 = admin.create_account("Chanchol Kumar Modok", initial_balance = 10000, loan_limit = 50000)
person2 = admin.create_account("Jhankar Mahbub", initial_balance = 20000, loan_limit = 90000)

person1.deposit(5000)
person1.withdraw(3000, Admin.check_bank_balance())
person1.transfer(person2, 4000)

loan_amount = person2.get_loan()

print(f"{person1.name}'s Balance: {person1.check_balance()} ৳")
print(f"{person2.name}'s Balance: {person2.check_balance()} ৳")
print(f"Bank Balance: {admin.check_bank_balance()} ৳")
print(f"Total Loan Amount: {admin.check_total_loan_amount()} ৳")
print(f"{person1.name}'s Transaction History: {person1.check_transaction_history()}")
print(f"{person2.name}'s Transaction History: {person2.check_transaction_history()}")

admin.toggle_loan_feature(False)
loan_amount_after_disabled = person2.get_loan()
print(f"{person2.name}'s Loan Amount After Disabling Loan Feature: {loan_amount_after_disabled} ৳")
