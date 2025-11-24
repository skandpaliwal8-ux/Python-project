import random
def edit_board(position,board):
    #king black board black piece white board white peice
    piece=["| ⛁ ","│ ░ ","│ ○ ", "│ ▓ ","│ ● "]
    for i in range(len(board)):
        if i==0:
            continue
        for j in range(len(board[i])):
            if j==0:
                continue
            # set default square (light/dark)
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                board[i][j]=piece[3]
            else:
                board[i][j]=piece[1]
            # check black pieces (player 0)
            for k in position[0]:
                if k[0]==i and k[1]==j:
                    if k[2]==1:
                        board[i][j]=piece[0]
                    else:
                        board[i][j]=piece[2]
                    break
            # check white pieces (player 1)
            for k in position[1]:
                if k[0]==i and k[1]==j:
                    if k[2]==1:
                        board[i][j]=piece[0]
                    else:
                        board[i][j]=piece[4]
                    break
    return board

def possible_moves(position, player, r, c):
    moves = []
    captures = []
    if player == 0: 
        directions = [(1, -1), (1, 1)]
    else:  
        directions = [(-1, -1), (-1, 1)]
    king = 0
    t=0
    for p in position[player]:
        if p[0] == r and p[1] == c:
            king = p[2]
            t=1
            break
    if t==0:
        return moves,captures
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
    if moves!=[]:
        print(r,c,"can move to",moves)
    return moves, captures

def forced_move(position, player):
    forced = []
    pos_moves={}
    for piece in position[player]:
        r, c, k = piece
        t=f"{r} {c}"
        moves, captures = possible_moves(position, player, r, c)
        pos_moves[t]=moves
        if captures:
            forced.append([r, c])
    return forced,pos_moves

def queen(position,move):
    for i in position[move]:
        if move==0:
            if i[0]==8:
                i[2]=1
        if move==1:
            if i[0]==1:
                i[2]=1
    return position

def update_position(position, old_r, old_c, new_r, new_c, player):
    cap = False
    for piece in position[player]:
        if piece[0] == old_r and piece[1] == old_c:
            piece[0] = new_r
            piece[1] = new_c
            break
    # detect and remove captured piece (capture if moved by 2)
    if abs(new_r - old_r) == 2 and abs(new_c - old_c) == 2:
        po1 = old_r + (new_r - old_r)//2
        po2 = old_c + (new_c - old_c)//2
        other = 1 - player
        for enemy in position[other]:
            if enemy[0] == po1 and enemy[1] == po2:
                position[other].remove(enemy)
                cap = True
                break
    return position, cap

def win(position):
    if position[0]==[]:
        print("Player2 wins")
        return 0
    elif position[1]==[]:
        print("Player1 wins")
        return 0

def input_moves(prompt_text="Enter move: "):
    move_input=input(prompt_text).split()
    cords=[]
    for i in move_input:
        if i.isdigit()==True:
                cords.append(int(i))
                continue
        elif ("".join(move_input)).lower()=="save":
                print("Initiation save sequence")
                return 1
        else:
                print("Enter correct input")
                return 0
    if len(cords) < 2:
        print("Enter correct input")
        return 0
    if cords[0]>8 or cords[1]>8 or cords[0]<1 or cords[1]<1:
        print("Out of board! Enter the move again")
        return 0
    return cords


def inverse(player):
    if player==0:
        return 1
    else:
        return 0

def bot_select(forced,pos_moves):
    if forced:
        key = f"{forced[0][0]} {forced[0][1]}"
        moves = pos_moves[key]
        chosen = random.choice(moves)
        return [forced[0][0], forced[0][1]], chosen
    items = [(k,v) for k,v in pos_moves.items() if v]
    if not items:
        return None
    key, moves = random.choice(items)
    r, c = map(int, key.split())
    chosen = random.choice(moves)
    return [r, c], chosen
        

def edit_board(position,board):
    #king black board black piece white board white peice
    piece=["| ⛁ ","│ ░ ","│ ○ ", "│ ▓ ","│ ● "]
    for i in range(len(board)):
        if i==0:
            continue
        for j in range(len(board[i])):
            if j==0:
                continue
            # set default square (light/dark)
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                board[i][j]=piece[3]
            else:
                board[i][j]=piece[1]
            # check black pieces (player 0)
            for k in position[0]:
                if k[0]==i and k[1]==j:
                    if k[2]==1:
                        board[i][j]=piece[0]
                    else:
                        board[i][j]=piece[2]
                    break
            # check white pieces (player 1)
            for k in position[1]:
                if k[0]==i and k[1]==j:
                    if k[2]==1:
                        board[i][j]=piece[0]
                    else:
                        board[i][j]=piece[4]
                    break
    return board

def possible_moves(position, player, r, c):
    moves = []
    captures = []
    if player == 0: 
        directions = [(1, -1), (1, 1)]
    else:  
        directions = [(-1, -1), (-1, 1)]
    king = 0
    t=0
    for p in position[player]:
        if p[0] == r and p[1] == c:
            king = p[2]
            t=1
            break
    if t==0:
        return moves,captures
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
    if moves!=[]:
        print(r,c,"can move to",moves)
    return moves, captures

def forced_move(position, player):
    forced = []
    pos_moves={}
    for piece in position[player]:
        r, c, k = piece
        t=f"{r} {c}"
        moves, captures = possible_moves(position, player, r, c)
        pos_moves[t]=moves
        if captures:
            forced.append([r, c])
    return forced,pos_moves

def queen(position,move):
    for i in position[move]:
        if move==0:
            if i[0]==8:
                i[2]=1
        if move==1:
            if i[0]==1:
                i[2]=1
    return position

def update_position(position, old_r, old_c, new_r, new_c, player):
    cap = False
    for piece in position[player]:
        if piece[0] == old_r and piece[1] == old_c:
            piece[0] = new_r
            piece[1] = new_c
            break
    # detect and remove captured piece (capture if moved by 2)
    if abs(new_r - old_r) == 2 and abs(new_c - old_c) == 2:
        po1 = old_r + (new_r - old_r)//2
        po2 = old_c + (new_c - old_c)//2
        other = 1 - player
        for enemy in position[other]:
            if enemy[0] == po1 and enemy[1] == po2:
                position[other].remove(enemy)
                cap = True
                break
    return position, cap

def win(position):
    if position[0]==[]:
        print("Player2 wins")
        return 0
    elif position[1]==[]:
        print("Player1 wins")
        return 0

def input_moves(prompt_text="Enter move: "):
    move_input=input(prompt_text).split()
    cords=[]
    for i in move_input:
        if i.isdigit()==True:
                cords.append(int(i))
                continue
        elif ("".join(move_input)).lower()=="save":
                print("Initiation save sequence")
                return 1
        else:
                print("Enter correct input")
                return 0
    if len(cords) < 2:
        print("Enter correct input")
        return 0
    if cords[0]>8 or cords[1]>8 or cords[0]<1 or cords[1]<1:
        print("Out of board! Enter the move again")
        return 0
    return cords


def inverse(player):
    if player==0:
        return 1
    else:
        return 0

def bot_select(forced,pos_moves):
    if forced:
        k=random.choice(forced)
        return k,[]
    items = [(k,v) for k,v in pos_moves.items() if v]
    if not items:
        return None
    key, moves = random.choice(items)
    r, c = map(int, key.split())
    chosen = random.choice(moves)
    return [r, c], chosen
