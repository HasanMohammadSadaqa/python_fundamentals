class User:
    def __init__(self, name):
        self.name = name			
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


saeed = User("Saeed")
hasan = User("Hasan")
maram = User("Maram")
saeed.make_deposit(100)
saeed.make_deposit(100)
saeed.make_deposit(100)
saeed.make_withdrawal(50)
saeed.display_user_balance()

hasan.make_deposit(100)
hasan.make_deposit(100)
hasan.make_withdrawal(50)
hasan.make_withdrawal(50)
hasan.display_user_balance()

maram.make_deposit(1000)
maram.make_withdrawal(50)
maram.make_withdrawal(50)
maram.make_withdrawal(50)
maram.display_user_balance()

saeed.transfer_money(maram, 25)
saeed.display_user_balance()
maram.display_user_balance()