import random
symbols=[ "🐷", "🤑", "🎃", "🧵", "♥", "♠", "♣", "♦", "🎄", "✂", "🧁","💜", "🔠"]

Wallet= 100

def slot_machine():
    global Wallet
    money= int(input("Insert $1 to play (type 1) "))
    Wallet-=money
    print(Wallet)
    bet= float(input("How much do you want to bet? ($1 minimum, don't type $ sign) "))
    spin= input("Type spin to spin ")
    if spin=="spin":
        for i in range(4):
            row=random.sample(symbols, 3)
            print(row)
            if row== ["🤑", "🤑", "🤑"] or row==["♥", "♠", "♣"] or row==["♠", "♣", "♦"] or row==["✂", "🧁","💜"]:
                print("Somehow, you won. Yay... ")
                result="Win"
            else:
                print("nope")
                result="Loss"
    if result=="Win":
        Wallet+=bet
        print(Wallet)
    elif result=="Loss":
        Wallet-=bet
        print(Wallet)
    else:
        raise Exception("How did we get here? ")

    
def bar():
    global Wallet
    Menu={
        "Champagne" : 3,
        "Beer": 3,
        "Red Wine": 3.50,
        "White Wine": 3.50,
        "Whiskey": 4,
        "Liquor": 4,
        "Pretzels": 5
    }
    print("Menu")
    for item, price in Menu.items():
        print(item,": $", price)
    sales_tax= 1.0725
    total_price=0
    reciept={
    }
    order=input("Order Here or Type 'exit' to exit ").title()
    while order!="exit":
        num=int(input("How many of this item? "))
        total_price+=Menu[order]*num
        reciept[order + ' x ' + str(num)] = round((Menu[order]*num), 2)
        order=input("Order Here or Type 'exit' to exit ")
    subtotal= total_price
    after_tax= round( total_price*sales_tax, 2)
    print("Total Price: $", total_price)
    print("Receipt")
    for item, price in reciept.items():
        print(item,": $", price)
    print("Subtotal: ", "$", subtotal)
    print("Tax: ", str(round((sales_tax-1)*100,2))+"% ")
    print("Total After Tax: ", "$", after_tax)
    Wallet-=after_tax

def roulette():
    global Wallet
    Wallet-= 1
    your_bet=float(input("How much do you bet, minimum $1, don't type sign "))
    your_guess=int(input("Pick a number between 1-25 "))
    computers_guess=random.randint(1, 25)
    print(computers_guess)
    if your_guess==computers_guess:
        print("yay you won ")
        Wallet+=your_bet
        print(Wallet)
    else:
        print("Nope ")
        Wallet-= your_bet

def Lounge():
    global Wallet
    lounge_choice=input(("the baSIc lounGe costs no Money. Unless you know the pAssword to the secret one- then you can upgrade :)  "))
    if lounge_choice=="SIGMA":
        print("wOw, you figured it out, how smart of you. We've deducted the fee already. Enjoy. ")
        Wallet-=0.01
        mysterious_box=input("Would you like to open the mysterious box? Y or N ")
        if mysterious_box=="Y":
            print("You just unlocked a chest full of posionous spiders. Insurance doesn't cover the medical bills.")
            Wallet-= 1000
        else:
            print("Okay. Whatever")
    else:
        print("Nahhhhh you're stuck here")
        


age= input("Are you 21+ years of age? Y or N ")
if age== "N":
    print("Go away, minor. ")
    start=False
else:
    start= True
while start!=False:
    choice=input("What do you want to do? Bar, Slot Machine, Roulette, Lounge ").lower()
    if choice=="slot machine":
        slot_machine()
    elif choice== "bar":
        bar()
    elif choice=="roulette":
        roulette()
    elif choice=="lounge":
        Lounge()
    if Wallet==0:
        print("You are at 0 balance! ")
        leaving=input("Do you want to go into debt? Y or N")
        if leaving=="N":
            print("awwwwwwwwww. Thanks for spending with us, hope to see you again soon!")
            start=False
        else:
            print("That's what we thought!!!!!" )
        
    