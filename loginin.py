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
        birthday= input("Birthday: ")
        email= input("Email: ")
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



