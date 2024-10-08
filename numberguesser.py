import random, time
def get_input_from_user() :
    s=time.time()
    guess=int(input("Guess number between 1-257 "))
    e=time.time()
    return e-s, guess
mysterynumber= random.randint(1,257)
trime,response=get_input_from_user()
counter=1


while response !=mysterynumber:
    counter+=1
    print("Try again please ") 
    if trime>7.789:
        print(trime, "secs. L, you lost... to time.  ")
    elif response> mysterynumber:
        print("Too high. You failed ")
    else:
        print("Too low. Aim higher ")
    trime,response=get_input_from_user()


print("You got it right... finally. ")
print(counter,"Tries it took you to finally succeed... about time ")
print(trime,"secs was your time ")
