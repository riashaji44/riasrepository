from bank_account import BankAccount

account1 = BankAccount(123456)
account2 = BankAccount(7654321, 150.00)
account3 = BankAccount(3232323, 584.73)

print(account1)
print(account2)
print(account3)
print()

account1.deposit (500)
account2.withdraw (3000)
account3.deposit(0)
account3.withdraw(100)
account1.get_balance
account2.get_balance
account3.get_balance


