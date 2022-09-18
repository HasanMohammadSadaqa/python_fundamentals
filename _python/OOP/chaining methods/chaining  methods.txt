class User:
    def __init__(self, name):
        self.name = name			
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


saeed = User("Saeed")
hasan = User("Hasan")
maram = User("Maram")

saeed.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

hasan.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()

maram.make_deposit(1000).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

saeed.transfer_money(maram, 25).display_user_balance()
maram.display_user_balance()