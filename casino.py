import random
symbols=[ "🐷", "🤑", "🎃", "🧵", "♥", "♠", "♣", "♦", "🎄", "✂", "🧁","💜", "🔠"]


def slot_machine():
    money= input("Insert $1 to play (type 1) ")
    bet= input("How much do you want to bet? ($1 minimum, don't type $ sign) ")
    spin= input("Type spin to spin ")
    if spin=="spin":
        for i in range(4):
            row=random.sample(symbols, 3)
            print(row)
            if row== ["🤑", "🤑", "🤑"] or row==["♥", "♠", "♣"] or row==["♠", "♣", "♦"] or row==["✂", "🧁","💜"]:
                print("Somehow, you won. Yay... ")
            else:
                print("nope")


     


    


age= input("Are you 21+ years of age? Y or N ")
if age== "N":
    print("Go away, minor. ")
else:
    slot_machine()
    