import random
class Account:
    def __init__(self, name, email, number, balance  ):
        self.name=name
        self.email= email
        self.number= number
        self.balance= balance

    def deposit(self, amount):
            if int(amount)>0:
                self.balance+=int(amount)
                print("You have deposited money. ")
            elif amount<=0:
                print("Error. Deposit positive values only. ")

    def withdraw(self, amount):
            if amount>self.balance:
                print("Error. Ask too high. Try again. ")
            elif amount <0:
                print("Error. Amount is negative. Try wth a positive number ")
            else:
                self.balance-=amount
                print("Transaction sucessful. You have withdrawn money. ")

    def see_balance(self):
            print("Balance: $"+ str(self.balance))

    def display_account_details(self):
         print(self.name, self.balance, self.number, self.balance)

class Bank:
    def __init__(self):
        self.accounts={}
    def create_account(self, name, email, number, balance):
        if number in self.accounts:
            print("Account already exists ")
        else:
            account=Account(name, email, number, balance)
            self.accounts[number]=account
            account.display_account_details()
            print("Sucess! You have created an account! Enjoy while you collect intrest off of our misery!")            
    def delete_account(self, number):
        if number not in self.accounts:
            print("Account not found. ")
        else:
            del self.accounts[number]
            print("Account deleted... We're sad to see you go :(((")
    def display_account(self, name, email, number, balance):
        print("Name:"+ self.name +"Email:"+ self.email +"Account number:"+ self.number +"Account balance:"+ self.balance)
    def display_all_accounts(self):
        for i in self.accounts.values():
            i.display_account()

    def all_accounts(self):
         return self.accounts
    
    def all_account_nums(self):
         return list(self.accounts.keys())


shriyasbank= Bank()

users= input("Are you a new or returning customer? ")
if users=="new":
     print("Creating account. ")
     name= input("What is your name? ")
     email=input("Beautiful name. What is your email? ")
     accountnumber=random.randint(0, 10000)
     while accountnumber in shriyasbank.all_account_nums():
          accountnumber=random.randint(0, 10000)
     balance= 0

     shriyasbank.create_account(name, email, accountnumber, balance)

     nextaction= input("What do you want to do? Deposit, withdraw, or see balance? ")
else:
     nextaction= input("What do you want to do? Deposit, withdraw, or see balance? ")

while True:
    if nextaction=="Deposit":
        accountnumber=int(input("What is your account number? "))
        depositval= float(input("How much do you want to deposit? $"))
        shriyasbank.all_accounts()[accountnumber].deposit(depositval)
    elif nextaction=="Withdraw":
        accountnumber=int(input("What is your account number?"))
        withdrawval= float(input("How much do you want to withdraw? $"))
        shriyasbank.all_accounts()[accountnumber].withdraw(withdrawval)
    else:
        accountnumber=int(input("What is your account number?"))
        shriyasbank.all_accounts()[accountnumber].see_balance()
    nextaction= input("What do you want to do? Deposit, withdraw, or see balance? ")





