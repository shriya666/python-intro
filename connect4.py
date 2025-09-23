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
        else:
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
        else:
            in_a_red_column=0

def horizontal_win(row: int):
    in_a_yellow_row=0
    for col in range(5):
        if board[row][col]=="🟡":
            in_a_yellow_row+=1
            if in_a_yellow_row==4:
                print("Yellow won!!!! ")
                game==False
                break
        else:
            in_a_yellow_row=0

def horizontal_red_win(row: int):
    in_a_red_row=0
    for col in range(5):
        if board[row][col]=="🔴":
            in_a_red_row+=1
            if in_a_red_row==4:
                print("Red won!!!! ")
                game==False
                break
        else:
            in_a_red_row=0

def diaganol_some_color_win(row, col, color):
    in_a_diaganol=0
    for col in reversed(range(1, 5)):
        if board[row][col]==color:
            in_a_diaganol+=1
        if row+1>=len(board):
            break
        if in_a_diaganol==4:
            print( "You won!!!!")
            #     else:
            #         in_a_diaganol = 0
        row += 1
        col += 1
        print(row, col)

# def in_a_different_diaganol(row, col, color):
#     in_a_diaganol=0
#     for col in range(1, 5, 2):
#         if board[row][col]==color:
#             if row+1<=len(board)-1:
#                 if board[row+1][col+1]==color:
#                     in_a_diaganol+=1
#                 else:
#                     in_a_diaganol = 0
#             else:
#                 break

def down_yellow_win(row, col):
    in_a_down_diaganol= 0
    for col in reversed(range(1, 5, 2)):
        if board[row][col]=="🟡":
            in_a_diaganol+=1
            if row+1<=len(board):
                if board[row+1][col+1]=="🟡":
                    in_a_diaganol+=1
                else:
                    in_a_diaganol = 0
            else:
                break



        

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
    horizontal_win(empty_row)
    diaganol_some_color_win(empty_row, column, "🟡")
    diaganol_some_color_win(empty_row, column, "🔴")
    # in_a_different_diaganol(empty_row, column, "🟡" )
    # in_a_different_diaganol(empty_row, column, "🔴" )
    move= int(input ("Which column? 1, 2, 3, 4, or 5? "))
    r = find_bottom(move-1)
    board[r][move-1]= "🔴"
    for i in board:
        print(i)
    red_won(move-1)
    horizontal_red_win(r)
    


            










    









