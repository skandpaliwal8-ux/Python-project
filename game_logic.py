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
#function for getting the possible moves
def possible_moves(position,player,r,c,l):
    moves=[]
    captures=[]
    if player == 0: 
        dir=[(1,-1),(1,1)]
    else:  
        dir=[(-1,-1),(-1,1)]
    king=0
    t=0
    for p in position[player]:
        if p[0]==r and p[1]==c:
            king=p[2]
            t=1
            break
    if t==0:
        return moves,captures
    if king==1:
        dir=[(1,-1),(1,1),(-1,-1),(-1,1)]
    enemy=1-player
    for x1,y1 in dir:
        x2=r+x1
        y2=c+y1
        if 1<=x2<=8 and 1<=y2<=8:
            occupied=False
            for p in position[0]+position[1]:
                if p[0]==x2 and p[1]==y2:
                    occupied=True
                    break
            if not occupied:
                moves.append([x2,y2])
        x3=r+x1
        y3=c+y1
        x4=r+2*x1
        y4=c+2*y1
        if 1<=x4<=8 and 1<=y4<=8:
            enem=False
            for p in position[enemy]:
                if p[0]==x3 and p[1]==y3:
                    enem=True
                    break
            if enem:
                land=True
                for p in position[0]+position[1]:
                    if p[0]==x4 and p[1]==y4:
                        land=False
                        break
                if land:
                    captures.append([x4,y4])
    if moves!=[] and captures==[]:
        if (l==1 and player!=1) or l==2:
            print(r,c,"can move to",moves)
    return moves, captures

#for checking if forced moves are there
def forced_move(position, player,l):
    forced=[]
    pos_moves={}
    for piece in position[player]:
        x1, x2, k = piece
        t=f"{x1} {x2}"
        moves, captures = possible_moves(position, player,x1,x2,l)
        pos_moves[t]=moves
        for i in captures:
            forced.append([[x1,x2],i])
    #pos_moves contains all moves for each piece
    return forced,pos_moves

#for making king
def queen(position,move):
    for i in position[move]:
        if move==0:
            if i[0]==8:
                i[2]=1
        if move==1:
            if i[0]==1:
                i[2]=1
    return position

def update_position(position,x1,y1,x2,y2,player):
    #cap is if piece captured
    cap=False
    for piece in position[player]:
        if piece[0]==x1 and piece[1]==y1:
            piece[0]=x2
            piece[1]=y2
            break
    #detecting piece capture
    if abs(x2-x1)==2 and abs(y2-y1)==2:
        po1=x1+(x2-x1)//2
        po2=y1+(y2-y1)//2
        other=1-player
        for enemy in position[other]:
            if enemy[0]==po1 and enemy[1]==po2:
                position[other].remove(enemy)
                cap=True
                break
    return position,cap
#check win
def win(position):
    if position[0]==[]:
        print("Player2 wins")
        return 0
    elif position[1]==[]:
        print("Player1 wins")
        return 0
#inputting moves from user
def input_moves(a="Enter move: "):
    move_input=input(a).split()
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
    if len(cords)<2:
        print("Enter correct input")
        return 0
    if cords[0]>8 or cords[1]>8 or cords[0]<1 or cords[1]<1:
        print("Out of board! Enter the move again")
        return 0
    return cords

#changes between player1 and 2
def inverse(player):
    if player==0:
        return 1
    else:
        return 0
#bot selecting movevs function
def bot_select(forced,pos_moves):
    if forced!=[]:
        s=random.choice(forced)
        return s[0],s[1]
    items = [(k,v) for k,v in pos_moves.items() if v]
    if not items:
        return None
    key,moves=random.choice(items)
    a,b=map(int, key.split())
    chosen=random.choice(moves)
    return [a, b], chosen