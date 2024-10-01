import random
mysterynumber= random.randint(1,100)
guess=int(input("Guess number between 1-100 "))


while guess !=mysterynumber:
    print("Try again please ") 
    if guess> mysterynumber:
        print("Too high. You failed ")
    else:
        print("Too low. Aim higher ")
    guess=int(input("Guess number between 1-100 "))


print("You got it right... finally. ")