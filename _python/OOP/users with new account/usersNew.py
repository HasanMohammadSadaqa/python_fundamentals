class User:
    def __init__(self, name):
        self.name = name
        self.account = [BankAccount(interest_value=0.02, balance=0)]	
    def create_new_account(self):
        self.account.append(BankAccount(interest_value=0.02, balance=0))
        return self
    def make_deposit(self, amount, acc_number):
        self.account[acc_number].deposit(amount)
        return self
    def make_withdrawal(self, amount, acc_number):
        self.account[acc_number].withdraw(amount)
        return self
    def display_user_balance(self, acc_number):
        print('Name: ', self.name)
        self.account[acc_number].display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

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
        print('Balance:', self.balance)
        return self
    def yeild_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.interest_value)
        return self


hasan = User('hasan')
hasan .make_deposit(1000, 0).make_withdrawal(100, 0).display_user_balance(0)
hasan .create_new_account().make_deposit(500, 1).display_user_balance(1)
hasan .create_new_account().make_deposit(5000, 2).display_user_balance(2)