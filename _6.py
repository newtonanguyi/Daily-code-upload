class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, interest_rate=0.03):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited UGX {amount} to account UGX '{self.account_number}'.\nCurrent account balance is UGX {self.balance}")
        print("-"*60)
        print('\n')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn UGX {amount} from account UGX '{self.account_number}'.\nCurrent account balance is UGX {self.balance}")
            print('\n')
        else:
            print(f"Cannot withdraw UGX {amount} since it exceeds your current account balance.")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nCurrent Balance: {self.balance}")

sav1 = SavingsAccount('9845628351', 300000000, 'John Lick')
sav2 = SavingsAccount('3452634522', 5000000000, 'Anguyi Newton')


sav1.deposit(20000000)
sav2.withdraw(6000000000)

print("-"*60)
sav1.display_account_info()
print("-"*60)
sav2.display_account_info()