
import random
words1=[
    "computer",
    "cheese",
    "mouse",
    "chair",
    "laptop",
    "phone",
    "ipad",
    "monitor"

]
words2=[
    "cake",
    "camera",
    "canvas",
]
words3=[
    "defenestrate",
    "retaliate"
    "representative"
]
level=1

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

if level == 1:
    word= random.choice(words)
    blanks= []
    for i in word:
        blanks.append("_")
    errors= 0
    while "_" in blanks:
        print("".join(blanks))
        guess= input("Guess a letter ")
        if guess in word:
            # blanks[word.index(guess)]=guess
            for i in range (len (word)):
                if word [i]==guess:
                    blanks[i]=guess
        else:
            print("Try again ")
            errors+=1
        if errors>= len (HANGMANPICS):
            print("You are a dissapointment to society. Good bye. ")
            break
        print(HANGMANPICS[errors])
    if "_" not in blanks:
        print("You did it!")
        print(word)
        print(errors)
        level+=1
        moving=True
if level==2 and moving==True:
   word= random.choice(words)
    blanks= []
    for i in word:
        blanks.append("_")
    errors= 0
    while "_" in blanks:
        print("".join(blanks))
        guess= input("Guess a letter ")
        if guess in word:
            # blanks[word.index(guess)]=guess
            for i in range (len (word)):
                if word [i]==guess:
                    blanks[i]=guess
        else:
            print("Try again ")
            errors+=1
        if errors>= len (HANGMANPICS):
            print("You are a dissapointment to society. Good bye. ")
            break
        print(HANGMANPICS[errors])
    if "_" not in blanks:
        print("You did it!")
        print(word)
        print(errors)
        level+=1
        moving=True 

        

