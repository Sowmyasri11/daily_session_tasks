'''
A bank wants to design a system to manage different types of accounts.
Scenario:
Create a base class Account with attributes account_number and balance
Create subclasses SavingsAccount and CurrentAccount
Requirements:
Implement deposit() and withdraw() in the base class
Override withdraw() in SavingsAccount to enforce minimum balance
Override withdraw() in CurrentAccount to allow overdraft up to a limit
Demonstrate runtime polymorphism using a common interface
'''


class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.__balance = 150000

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

#Inheritining Account class
class SavingsAccount(Account):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    #overriding withdraw method and providing extra functionality(if amount is less than balance raise error)
    def withdraw(self, amount):
        if amount < self.__balance:
            raise ValueError("Please check you current balance")
        self.__balance -= amount

#Inheriting Account class
class CurrentAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    #overriding withdraw method (if amount is greater than limit raise an error)
    def withdraw(self, amount):
        if amount < 50000:
            raise ValueError("Sorry! You can't withdraw more than 50000")
        self.__balance -= amount


def main():
    account_type = input("Enter the type of account(SavingsAccount/CurrentAccount):")
    if account_type == "SavingsAccount":
        account_number = int(input("Enter account number:"))
        choice = input("withdraw/deposit")
        if choice == "withdraw":
            amount = int(input("Enter amount:"))
            SavingsAccount.withdraw(amount)
        elif choice == "deposit":
            amount = int(input("Enter amount to deposit:"))
            SavingsAccount.deposit(amount)
    elif account_type == "CurrentAccount":
        account_number = int(input("Enter account number :"))
        choice = input("deposit/withdraw")
        if choice == "deposit":
            amount = int(input("Enter amount to  deposit:"))
            CurrentAccount.deposit(amount)
        elif choice == "withdraw":
            amount = int(input("Enter amount to withdraw:"))
            CurrentAccount.withdraw(amount)


if __name__ == "__main__":
    main()
