from datetime import date
class User:
    def __init__(self, name, username, password, birthday, email):
        self.name= name
        self.username= username
        self.password= password
        self.birthday=birthday
        self.email=email
    def __str__(self):
        return f"{self.name}-- {self.username}--{self.birthday}"
    
Users=[]

while True:
    option=input("Log in or Sign up? ")
    if option=="Sign up":
        name= input("Name: ")
        username= input("Username: ")
        userfound= False
        for user in Users:
            if user.username==username:
                userfound=True 
        while userfound==True:
            print("Username already exists. Begone, and respawn. ")
            username= input("Username: ")
            userfound= False
            for user in Users:
                if user.username==username:
                    userfound=True 

        birthday= input("Birthday mm/dd/yyyy: ")
        
        if date.today().year- int(birthday[6:])<= 11:
            print("You are too smol for this world. Go back to your safety net. ")
            continue
        emailcheck= False
        email= input("Email: ")
        for user in Users:
            if user.email==email:
                emailcheck=True 

        if emailcheck==True:
            print("Email address already exists. Stop trying to cheat the system!")
            continue

        password= input("Password: ")
        cpass= input("Confirm Password: ")
        while password != cpass:
            print("Passwords do not match. ")
            password= input("Password: ")
            cpass= input("Confirm Password: ")    
        Users.append(User(name, username, password, birthday, email))
    else: 
        username= input("Username: ")
        password= input("Password: ")


        for user in Users:
            if user.username== username:
                if user.password==password:
                    print("You are logged in. Congratulations, you know your username and password. ")



