from board import board,print_board,position
board=board()
position=position()
def edit_board(postion,board):
    #king black board black piece white board white peice
    piece=["| ⛁ ","│ ░ ","│ ○ ", "│ ▓ ","│ ● "]
    for i in range(len(board)):
        if i==0:
            continue
        for j in range(len(board[i])):
            if j==0:
                continue
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                board[i][j]=piece[3]
            for k in position[0]:
                if k[2]==1:
                    board[i][j]=piece[0]
                if k[0]==i and k[1]==j:
                    board[i][j]=piece[2]
            for k in position[1]:
                if k[2]==1:
                    board[i][j]=piece[0]
                if k[0]==i and k[1]==j:
                    board[i][j]=piece[4]
    return board

def possible_moves(position, player, r, c):
    moves = []
    captures = []
    if player == 0: 
        directions = [(1, -1), (1, 1)]
    else:  
        directions = [(-1, -1), (-1, 1)]
    king = 0
    for p in position[player]:
        if p[0] == r and p[1] == c:
            king = p[2]
            break
    if king == 1:
        directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
    enemy = 1 - player
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if 1 <= nr <= 8 and 1 <= nc <= 8:
            occupied = False
            for p in position[0] + position[1]:
                if p[0] == nr and p[1] == nc:
                    occupied = True
                    break
            if not occupied:
                moves.append([nr, nc])
        er = r + dr
        ec = c + dc
        jr = r + 2*dr
        jc = c + 2*dc
        if 1 <= jr <= 8 and 1 <= jc <= 8:
            enemy_here = False
            for p in position[enemy]:
                if p[0] == er and p[1] == ec:
                    enemy_here = True
                    break
            if enemy_here:
                landing_empty = True
                for p in position[0] + position[1]:
                    if p[0] == jr and p[1] == jc:
                        landing_empty = False
                        break
                if landing_empty:
                    captures.append([jr, jc])
    return moves, captures

def forced_move(position, player):
    forced = []
    pos_moves=[]
    for piece in position[player]:
        r, c, k = piece
        moves, captures = possible_moves(position, player, r, c)
        pos_moves.append(moves)
        if captures:
            forced.append([r, c])
    return forced,pos_moves

def queen(position,move):
    for i in position[move]:
        if move==0:
            if i[0]==8:
                i[2]=1
        if move==1:
            if i[0]==0:
                i[2]=1
    return position

def update_position(position, old_r, old_c, new_r, new_c, player):
    for piece in position[player]:
        if piece[0] == old_r and piece[1] == old_c:
            piece[0] = new_r
            piece[1] = new_c
            break
    other = 1 - player
    for enemy in position[other]:
        if enemy[0] == new_r and enemy[1] == new_c:
            position[other].remove(enemy)
            break
    return position

def win(position):
    if position[0]==[]:
        print("Player2 wins")
        return 0
    elif position[1]==[]:
        print("Player1 wins")
        return 0

def input_moves():
    move_input=input("Enter move: ").split()
    k=0
    cords=[]
    for i in move_input:
        if i.isdigit()==True or i.isspace()==True:
            if i.isdigit==True:
                cords[k]=int(i)
                continue
        elif move_input.lower()=="save":
            print("Initiation save sequence")
            return 1
        else:
            print("Enter correct input")
            return 0
    if cords[0]>8 or cords[1]>8 or cords[0]<0 or cords[1]<0:
        print("Out of board! Enter the move again")
        return 0
    return cords

def inverse(player):
    if player==0:
        return 1
    else:
        return 0

    return
#player1 is black player2 is white
def game():
    player=1
    c=0
    print("Top left represents (1 1). Enter the coordinates as (row column)")
    print("Type 'SAVE' to save the current game to continue playing it later")
    while True:
        player=inverse(player)
        print_board(board)
        forced,pos_moves= forced_move(position, player)
        if all(len(x) == 0 for x in pos_moves):
            print("Out of moves!!!!")
            print(f"{inverse(player)+1} wins!!")
            break
        if forced:
            print("u have to capture bitchass")
            print("pieces that must move:")
            for (r,c), caps in forced:
                print(f"piece at {r} {c} can capture to:", caps)
        print(f"It's player{player+1}'s turn")
        cords=input_moves()
        if isinstance(cords,int):
            if cords==1:
                break
            else:
                continue
        moves,captures=possible_moves(position,player,cords[0],cords[1])

        if moves==[]:
            print("Invalid move!")
            continue
        print("Your possible moves are:",[i for i in moves])
        if captures==[]:
            print("You don'r have any captures")
        else:
            print("Your possible captures are:",[i for i in captures])
        while True:
            cur=input_moves()
            if isinstance(cur,int):
                if cur==1:
                    continue
                else:
                    break
            if cur not in moves:
                print("SAhi chale yaar")
                continue
            else:
                break  
        position=update_position(position,cords[0],cords[1],cur[0],cur[1],player)
        position=queen(position,player)
        board=edit_board(position,board)
        win(position)

game()

  