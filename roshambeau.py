import random
def game():
    tryagain= input(" Type 'play' to start ")
    winner={
        "rock" : "paper",
        "scissors" : "rock",
        "paper": "scissors",
    }
    # while tryagain=="play":
    if tryagain!="play":
           game()

    CPU=random.choice( ["rock","scissors","paper" ])

    play= input(" rock, paper, scissors... Shoot! ")
    print("\x1b[32mThe computer played: \x1b[0m" + (CPU))

    beats = winner[play]

    if CPU == beats:
            print("You lost! New Game! ")
    elif play == CPU:
            print("Tie. Try again ")
    else:
            print("You beat the bot! New game! ")
    game()
game()