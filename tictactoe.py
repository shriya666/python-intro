
import random 
row1 = ["_", "_", "_"]
row2 = ["_", "_", "_",]
row3 = ["_", "_", "_",]

print(row1, row2, row3, sep="\n")

play= input("X or O ? ")
if play== "X":
    computer = "O"
    print("The computer is O ")
else:
    computer = "X"
    print("The computer is X ")

while True:
    row= input (" Which row do you want? row1, row2, or row3? ")
    column= int(input ("Which column? 1, 2, or 3? "))
    if row== "row1":
        row1[column- 1] = play
        print(row1, row2, row3)
    elif row=="row2":
        row2[column- 1] = play
        print(row1, row2, row3)
    else:
        row3[column- 1] = play
        print(row1, row2, row3)

    bot= random.randint(1, 3)
    bott= random.randint(1, 3)
    if bot== 1:
        row1[bott- 1] = computer

    elif bot== 2:
        row2[bott-1] = computer
    else:
        row3[bott-1]= computer

    print(row1, row2, row3)

    if row1[0] ==  row1[1] ==  row1[2] == "X":
        print(row1, row2, row3)
        exit()
    if row2[0] ==  row2[1] ==  row2[2] == "X":
        print(row1, row2, row3)
    if row3[0] ==  row3[1] ==  row3[2] == "X":
        exit()
    if row1[0] ==  row2[0] ==  row3[0] == "X":
        print(row1, row2, row3)
        exit()
    if row1[1] ==  row2[1] ==  row3[1] == "X":
        print(row1, row2, row3)
        exit()
    if row1[2] ==  row1[2] ==  row1[2] == "X":
        print(row1, row2, row3)
        exit()
    if row1[0] ==  row1[1] ==  row1[2] == "X":
        print(row1, row2, row3)
        exit()
    if row1[2] ==  row1[1] ==  row1[0] == "X":
        print(row1, row2, row3)
        exit()










