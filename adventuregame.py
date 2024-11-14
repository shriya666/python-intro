
def game ():
    print("You work for a secret society of spies. You have been sent on a mission to infiltrate the bad guys. Turns out the bad guys live in a pyramid...")
    choice1=input("How do you enter? \n a) locate a door and sneak in \n b) smash through the walls and enter \n c) disguise yourself as a bad guy and enter \n type letter.  ")
    if choice1== "a":
        print("No one noticed as you entered. Now you need to find the evil plans. ")
        choice1a= input("You sneak around and locate the main office. However, the door is surrounded by a moat of alligators. Do you a) find another entrance, or \n b) attempt to cross the moat? ")
        if choice1a== "a":
            choice2=input(" A bad guy mistakes you for a fellow bad guy and gives you an evil assignment, however your morals won't let you accept it (also it will distract from your mission). \n If you a) refuse, you might alert the bad guys that you are not who you say you are. \n But if you b) Take the assignment, you might have to harm your fellow good guys. ")  
            if choice2== "a":
                print("The bad guys find you suspicious, and they lock you up. ")
                choice3= input( "Do you \n a) Escape through tunelling or \n b) Escape through climbing. ")
                if choice3=="a":
                    print("There was no place to tunnel. You are surrounded. Bye-bye! ")
                else:
                    print("There is no place to climb. You are surrounded. Bye-bye! ")
        else:
            print("You safely cross. You recover the files. Success! ")
            Exit= input("Type 'exit' to restart ")
            if Exit== "exit":
                game()

    elif choice1=="b":
        print("The bad guys spotted you and killed you. Bye-bye! ")
        Exit= input("Type 'exit' to restart ")
        if Exit== "exit":
            game()
            
    else:
        print("You fooled the bad guys and they let you into their lair. Now you need to locate their evil plans. ")
        choice2=input(" A bad guy gives you an evil assignment, however your morals won't let you accept it (also it will distract from your mission). \n If you a) refuse, you might alert the bad guys that you are not who you say you are. \n But if you b) Take the assignment, you might have to harm your fellow good guys. ")
        if choice2== "a":
            print("The bad guys find you suspicious, and they lock you up. ")
            choice3= input( "Do you \n a) Escape through tunelling or \n b) Escape through climbing. ")
            if choice3=="a":
                print("There was no place to tunnel. You are surrounded. Bye-bye! ")
            
            else:
                print("There is no place to climb. You are surrounded. Bye-bye! ")
            Exit= input("Type 'exit' to restart ")
            if Exit== "exit":
                game()
        if choice2== "b":
            print(" You take the mission. The bad guy takes you to the office through a secert entrance. You are 3 feet away from the file with ALL the evil plans. ")
            choice4= input("Do you \n a) Fight the bad guy and forcibly take the file or \n b) Wait until the bad guy leaves to take it ")
            if choice4=="a":
                print(" That was dangerous! You lost and now you are dead. Bye-bye!")
                Exit= input("Type 'exit' to restart ")
                if Exit== "exit":
                    game()
            if choice4=="b":
                print("That was the smart move. You avoided confrontation. You have successfully completed your mission. ")
                Exit= input("Type 'exit' to restart ")
                if Exit== "exit":
                    game()

game()
