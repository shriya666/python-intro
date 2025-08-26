import random 

print("You are yellow. The computer is red. ")

board= [
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0,]
]


def find_bottom(col):
    if board[-1][col]==0:
        return 4

column= int(input ("Which column? 1, 2, 3, 4, or 5? "))

empty_row = find_bottom(column)


board[empty_row][column]="y"
for i in board:
    print(i)


def computers_move():
    move=random.randint(0, 4)
    find_bottom(move)
    return 

computers_move()








