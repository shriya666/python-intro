import random
import string
regenerate = "regenerate"
while regenerate == "regenerate":
    type= input("Numerical, Letter, Both or Both+?  ")
    length= input("How many characters? ")
    length=int(length)
    if type=="Numerical":
        characters = string.digits
    elif type=="Letter":
        characters = string.ascii_lowercase
    elif type=="Both":
        characters = string.digits + string.ascii_lowercase
    else:
        characters=  string.printable
    password1=""
    for i in range(length):
        d=random.choice(characters)
        password1+=d
    print(password1)
    regenerate= input("Type 'regenerate' to get another one. ")        


            
