class Account:
    def __init__(self,acc,bal):
        self.account=acc
        self.balance=bal
    def debit(self,amt):
        self.balance-=amt
        print("Your accout hase been debited by",amt)
        print("Your current amt is",self.balance)
    def credit(self,amt):
        self.balance+=amt
        print("Your accout hase been credited by",amt)
        print("Your current amt is",self.get_balance())
    def get_balance(self):
        return self.balance
A=Account(32943757,10000)
print("Your acc no",A.account)
A.debit(2000)
A.credit(7000)