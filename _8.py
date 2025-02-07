class AccountHolder:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class LoanAccount(AccountHolder):
    def __init__(self, name, age, address, loan_amount, loan_interest_rate):
        super().__init__(name, age, address)
        self.loan_amount = loan_amount
        self.loan_interest_rate = loan_interest_rate

    def apply_for_loan(self, amount):
        self.loan_amount += amount
        print(f"You have applied for a loan of UGX {amount}\nYour current loan amount is: {self.loan_amount}")
        print("-"*60)

    def repay_loan(self, amount):
        if amount <= self.loan_amount:
            self.loan_amount -= amount
            print(f"You have cleared UGX {amount} of your loan amount.\nYou're remaining with a balance of UGX {self.loan_amount - amount}")

        else:
            print(f"Your repay amount of UGX {amount} exceeds your loan balance of UGX {self.loan_amount}\nRefunding your UGX {amount - self.loan_amount}")

    def display_loan_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nLoan Amount: {self.loan_amount}")

loan1 = LoanAccount('Jack Maroon', 35, 'Wakiso', 0, 0.03)
loan1.apply_for_loan(300000)
loan1.repay_loan(400000)

print("-"*60)
loan1.display_loan_info()
