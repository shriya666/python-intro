class Account:
    def __init__(self, name, email, number, balance,  ):
        self.name=name
        self.email= email
        self.number= number
        self.balance= balance

    def deposit(self, ammount):
        if ammount>0:
            self.balance+=ammount
            print("You have deposited money. ")
        elif ammount<=0:
            print("Error. Deposit positive values only. ")
    def withdraw(self, ammount):
        if ammount>self.balance:
            print("Error. Ask to high. Try again. ")
        elif ammount <0:
            print("Error. Amount is negative. Try wth a positive number ")
        else:
            self.balance-=ammount
            print("Transaction sucessful. You have withdrawn money. ")
    def see_balance(self):
        print("Balance: "+self.balance)
class Bank:
    def __init__(self):
        self.accounts={
        }
    def create_account(self, name, email, number, balance):
        account=Account(name, email, number, balance)
        if number in self.accounts:
            print("Account already exists ")
        else:
            self.accounts[number]=account
            print("Sucess! You have created an account! Enjoy while we collect intrest off of your misery!")            
    def delete_account(self, number):
        if number not in self.accounts:
            print("Account not found. ")
        else:
            del self.accounts[number]
            print("Account deleted ")
    def display_account(self, name, email, number, balance):
        print("Name:"+ self.name +"Email:"+ self.email +"Account number:"+ self.number +"Account balance:"+ self.balance)
    def all_accounts(self):
        for i in self.accounts.values():
            i.display_account()
