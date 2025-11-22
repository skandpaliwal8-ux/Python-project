import time



def edit_board(postion,board):
    pass
    
def player_move(position,board):
    edit_board(position,board)

def print_board(board):
    for i in board:
        for j in i:
            print(j,end="")
        print("\n")

def queen(position,move,chance):
    for i in position[chance]:
        if move==0:
            if i[0]==8:
                i[2]=1
        if move==1:
            if i[0]==0:
                i[2]=1

    
def possible_moves(postion):
    pass 

def compulsory_move(position):
    pass

print_board(board)
def game():
    board=print_board()
    player=0
    print("Top left represents (1,1). Enter the coordinates as (row,column)")
    while True:
        print_board(board)
        print(f"It's player{player+1}'s turn")
        move_input=input("Enter move: ")
        
        if move_input[0]>8 or move_input[1]>8 or move_input[0]<0 or move_imput[1]<0:
            print("Out of board! Enter the move again")
            continue

        src, dst = move_input.split()

        try:
            sr, sc = parse_coord(src)
            tr, tc = parse_coord(dst)
        except:
            print("Invalid coordinates!")
            continue

        if not (in_bounds(sr, sc) and in_bounds(tr, tc)):
            print("Coordinates out of bounds.")
            continue

        result = try_move(board, sr, sc, tr, tc, player)

        if result == True:
            player = "black" if player == "white" else "white"

        elif result == "continue":
            # same player continues multi-jump
            continue

        else:
            # invalid move
            continue
