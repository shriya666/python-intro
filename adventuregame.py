
print("You work for a secret society of spies. You have been sent on a mission to infiltrate the bad guys. Turns out the bad guys live in a pyramid...")
choice1=input("How do you enter? \n a) locate a door and sneak in \n b) smash through the walls and enter \n c) you disguise yourself as a bad guy and enter \n type letter.  ")
if choice1== "a":
    print("No one noticed as you entered. Now you need to find the evil plans. ")
elif choice1=="b":
    print("The bad guys spotted you and killed you. Bye-bye! ")
else:
    print("You fooled the bad guys and they let you into their lair. Now you neede to locate their evil plans. ")
    choice2=input(" A bad guy gives you an evil assignment, however your morals won't let you accept it (also it will distract from your mission). \n If you a) refuse, you might alert the bad guys that you are not who you say you are. \n But if you b) Take the assignment, you might have to harm your fellow good guys. ")
    if choice2== "a":
        print("The bad guys find you suspicious, and they lock you up. ")
        choice3= input( "Do you \n a) Escape through tunelling or \n b) Escape through climbing. ")
        if choice3=="a":
            print("There was no place to tunnel. You are surrounded. Bye-bye! ")
        else:
            print("There is no place to climb. You are surrounded. Bye-bye! ")
