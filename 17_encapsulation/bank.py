# Doing Python Way Of Encapsulation (Not Strict Though)
# leaves it to the wisdom of the programmer
class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance # Private 

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")
    
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

account = BankAccount(1000)
print(account.balance)

account.deposit(3000)
print(account.balance)

account.withdraw(2000)
print(account.balance)