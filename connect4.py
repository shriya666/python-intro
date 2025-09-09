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
    if board[4][col]==0:
        return 4
    elif board[3][col]==0:
        return 3
    elif board [2][col]==0:
        return 2
    elif board[1][col]==0:
        return 1
    elif board[0][col]==0:
        return 0
    else:
        return False

def other_move():
    move= int(input ("Which column? 1, 2, 3, 4, or 5? "))
    r = find_bottom(move)
    board[r][move]= "🔴"
    return
def you_won(c):
    in_a_row=0
    for row in board:
        if row[c]== "🟡":
            in_a_row+=1
            if in_a_row==4:
                print("Yellow won!!!! ")
                game==False
                break
        if row[c]== "🔴":
            in_a_row= 0
def red_won(d):
    in_a_red_column=0
    for row in board:
        if row[d]== "🔴":
            in_a_red_column+=1
            if in_a_red_column==4:
                print("Red won!!!!!")
                game==False
                break
            if row[d]=="🟡":
                in_a_red_column=0
game= True 
while game==True: 
    column= int(input ("Which column? 1, 2, 3, 4, or 5? "))
    empty_row = find_bottom(column-1)
    if empty_row== False:
         print("Out of Bounds. Pick again. ")
    board[empty_row][column-1]="🟡"
    for i in board:
        print(i)
    you_won(column-1)
    move= int(input ("Which column? 1, 2, 3, 4, or 5? "))
    r = find_bottom(move-1)
    board[r][move-1]= "🔴"
    for i in board:
        print(i)
    red_won(move-1)

def horizontal_win():
    in_a_yellow_row=0
    if board[]






    









