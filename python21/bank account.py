"""This is a python
comment written in python copyright permission
applied if copied by someone not em"""
class Account:
    def __init__(self,account_no,name,balance,type):
        self.account_no=account_no
        self.name=name
        self.balance=balance
        self.type=type
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def get_balance(self):
        return self.balance
    def __str__(self):
        return self.name+ " "+self.account_no+ " "+str(self.balance)
acc1=Account('123','john',10.05,'current')
acc2=Account('345','john',23.55,'saving')
acc3=Account('567','phobe',12.5,'investment')
print(acc1)
print(acc2)
print(acc3)
acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance : ',acc1.get_balance())

