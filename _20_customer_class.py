class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Account:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited UGX'{amount}'. Your updated balance is UGX'{self.balance}'")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn UGX'{amount}'. Your updated balance is UGX'{self.balance}'")

        else:
            print(f"You cannot withdraw Ugx'{amount}' since it exceeds your current account balance.")

    def display_account_balance(self):
        print("-"*60)
        print(f"Account Number: {self.account_number}\nBalance: {self.balance}\nAccount Type: {self.account_type}")



customer = Customer('Anguyi', 'anguyi@gmail.com', '0750575911')
acc1 = Account('A32112', 2000000000, 'Savings')
acc2 = Account('B65412', 5000000000, 'Student')

acc1.deposit(3000000)
acc1.withdraw(2000000)

acc2.deposit(50000000)
acc2.withdraw(30000000)

acc1.display_account_balance()
acc2.display_account_balance()

