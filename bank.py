"""Challenge - 1

Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 

 """

class bank ():
    def __init__ (self,account_holder_name,account_number,initial_balance=0.0):
        self.__account_holder_name=account_holder_name
        self.__account_number=account_number
        self.__account_balance=initial_balance
        
    
    def deposit(self,cash):
        self.cash=cash
        if self.cash>0:
            self.__account_balance+=self.cash
            print(f"Deposited the amount rupees {cash}, your new Balance is {self.__account_balance}")
        else:
            print("you have entered a invalid amount")
    
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>0 and self.amount<=self.__account_balance:
            self.__account_balance-=self.amount
            print(f"withraw rupees {self.amount}, New balance is rupees {self.__account_balance}")
        else:
            print("you have entered a invalid or a insufficient amount")
    
    def display_balance(self):
        print(f"Account holder {self.__account_holder_name} your account number {self.__account_number} and your balance is rupees {self.__account_balance}")
        
s=bank("bala",2222222,200)

s.display_balance()
s.deposit(90)
s.withdraw(200)
