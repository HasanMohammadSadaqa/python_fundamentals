class BankAccount:
    def __init__(self, interest_value = 0.01, balance = 0):
        self.interest_value = interest_value
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.interest_value)
        return self

personalAccount = BankAccount(0.01,1000)
workAccount = BankAccount(0.02,5000)

# dummyAccount = BankAccount()
# dummyAccount.display_account_info()

personalAccount.deposit(500).deposit(500).deposit(500).withdraw(500).yeild_interest().display_account_info()
workAccount.deposit(100).deposit(100).withdraw(100).withdraw(50).withdraw(100).withdraw(50).yeild_interest().display_account_info()