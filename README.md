#Python project by Skand,Siddharth,Suryavenu
Python Project – Checkers Game

This is a simple implementation of the Checkers game in Python. It can be played between two players or between one player and a simple bot.

Project Features
Player versus Player mode
Player vs Bot mode
Text-based board display
Move validation including captures and king moves
Ability to save current game state
Ability to load a previously saved game
Modular structure: board handling, game rules, and file I/O in separate files.

Directory Structure
project/
│
├── board.py            # Handles the layout, printing, and position mapping of the board
├── file_manager.py     # Saving and loading game data using file I/O
├── game_logic.py       # Core game rules and move validation logic
├── main.py             # Main file that runs the game using all modules
├── text_checkers.txt   # Stores board positions for saved games

└── README.md           # Documentation

Game Instructions
Run the program through main.py.
Choose either Player vs Player or Player vs Bot.
The board will be displayed on the screen before each move.
When prompted, please specify the piece's starting position and the ending position where you'd like to move it to.
The program will check if the move is valid according to the rules of Checkers.
The system automatically handles captures, turn switching, and king movement.
You can save the game anytime. Loading will revert the board from the save file.

Setup Instructions
Requirements
Python 3.8 or later
No external libraries are needed

How to Run
Download the project folder.
Open a terminal in the project directory.

Use the following: python main.py The game will launch right away, and the program will take you through the rest.

Team members:
Skand: BA2025048
Siddharth: BA2025047
Suryavenu: 
