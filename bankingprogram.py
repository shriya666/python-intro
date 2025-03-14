class Account:
    def __init__(self, name, email, number, balance  ):
        self.name=name
        self.email= email
        self.number= number
        self.balance= balance
    job= input("What would you like to do? Deposit, Withdraw, or See Balance? ")
    print(job)
    if job=="Deposit":
        amount=input("How much to do you want to deposit? ")
        def deposit(self, amount):
            if int(amount)>0:
                self.balance+=int(amount)
                print("You have deposited money. ")
            elif amount<=0:
                print("Error. Deposit positive values only. ")
        print(deposit())
    elif job=="Withdraw":
        def withdraw(self, amount):
            if amount>self.balance:
                print("Error. Ask to high. Try again. ")
            elif amount <0:
                print("Error. Amount is negative. Try wth a positive number ")
            else:
                self.balance-=amount
                print("Transaction sucessful. You have withdrawn money. ")
    elif job=="See Balance":
        def see_balance():
            bal=input("what is yur balance ")
            print("Balance: "+bal)
        print(see_balance())
    else:
        print("Ask not understood. Perhaps you had a typo? ")
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
