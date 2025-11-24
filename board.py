def board():
    board = [
    ["    ", "  1 ", "  2 ", "  3 ", "  4 ", "  5 ", "  6 ", "  7 ", "  8 "], # Layout of the board using (number,number) coordinate system
    ["  1 ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● "],
    ["  2 ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ "],
    ["  3 ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● ", "│ ░ ", "│ ● "],
    ["  4 ", "│ ▓ ", "│ ░ ", "│ ▓ ", "│ ░ ", "│ ▓ ", "│ ░ ", "│ ▓ ", "│ ░ "],
    ["  5 ", "│ ░ ", "│ ▓ ", "│ ░ ", "│ ▓ ", "│ ░ ", "│ ▓ ", "│ ░ ", "│ ▓ "],
    ["  6 ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ "],
    ["  7 ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ "],
    ["  8 ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ ", "│ ○ ", "│ ░ "]
]
    return board
#starting position
def position():
    position = [
    [   # black pieces
        [1,2,0], [1,4,0], [1,6,0], [1,8,0],                      ##stores the coordinates of all the pieces on the board on the start,
        [2,1,0], [2,3,0], [2,5,0], [2,7,0],                      ## the first two numbers signify the coordinates of the piece
        [3,2,0], [3,4,0], [3,6,0], [3,8,0]                       ## the last number signifies whether the piece is a king or not 0 for not 1 if yes
    ],
    [   # whitew pieces
        [6,1,0], [6,3,0], [6,5,0], [6,7,0],
        [7,2,0], [7,4,0], [7,6,0], [7,8,0],
        [8,1,0], [8,3,0], [8,5,0], [8,7,0]
    ]
]
    return position

def print_board(board):
    for i in board:
        for j in i:
            print(j,end="")
        print("\n")
