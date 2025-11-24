import random
from board import board, position,print_board
from file_manager import load_game, save_game               ##imports all the functions required from the other files
board = board()
position = position()
from game_logic import edit_board, possible_moves, forced_move, update_position, queen, win, input_moves, inverse,bot_select

#player1 is black player2 is white
def main(board, position):
    print("Welcome to checkers!!!!")
    q=input("Load previous game? (Y/N): ").lower()              #basic interface when running the code that allows you to load a saved game
    player=0
    t=0
    if q=="y":
        lp,pl=load_game()
        if lp is not None:
            position=lp
            player=pl
    try:
        l=int(input("1. Bot\n2. 1v1\nChoose: "))
    except:
        l=2

    while True:
        board=edit_board(position, board)
        print_board(board)
        print(f"Player{player+1}'s turn")
        forced,pos_moves=forced_move(position,player,l)
        c=[]
        for i in forced:
            c.append(i[0])
        if all(len(x)==0 for x in pos_moves.values()):                                     #when the game ends
            print(f"Player{inverse(player)+1} wins!!")
            break

        if player==1 and l==1:
            start,end=bot_select(forced,pos_moves)
            if start is None:
                break
            moves,captures=possible_moves(position,player,start[0],start[1],l)
        else:
            cords=input_moves()
            if cords==1:
                save_game(position,player)
                break
            if not cords:
                continue
            start = cords
            moves,captures=possible_moves(position,player,start[0],start[1],l)
            if c and start not in c:
                print("Must capture.")
                continue
            print("Moves:", moves)
            print("Captures:", captures)
            cur=input_moves()
            if cur==1:
                save_game(position, player)
                continue
            end=cur
            if c and end not in captures:
                print("Must capture.")
                continue
            if not c and end not in moves:
                print("Invalid.")
                continue

        position,cap=update_position(position,start[0],start[1],end[0],end[1],player)
        position=queen(position, player)

        if cap:
            rr,cc=end
            while True:
                cmove,ccaps=possible_moves(position,player,rr,cc,l)
                if not ccaps:
                    break
                if player==1 and l==1:
                    nxt=random.choice(ccaps)
                else:
                    print("Next captures:", ccaps)
                    nxt=input_moves("Enter next capture: ")
                if nxt==1:
                    save_game(position, player)
                    continue                                                                   ##main function to run the game
                if nxt not in ccaps:
                    continue
                position,p=update_position(position,rr,cc,nxt[0],nxt[1],player)
                position=queen(position,player)
                rr,cc=nxt[0],nxt[1]

        k=win(position)
        if k==0:
            break
        player=inverse(player)

main(board,position)
