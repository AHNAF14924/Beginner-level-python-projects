# Tic-Tac-Toe Game

This is a simple implementation of the Tic-Tac-Toe game in Python. The game can be played between a user and a computer. The user gets to choose between X and O markers, and the computer takes turns automatically. The game continues until there is a winner or a tie.

## Getting Started

To run the program, make sure you have Python installed on your system. You can use any Python 3.x version. Follow these steps:

1. Copy the code provided into a Python file, e.g., tic_tac_toe.py.
2. Open a terminal or command prompt and navigate to the directory where the file is located.
3. Run the following command:
   `python tic_tac_toe.py`
   The game will start in the terminal, and you can follow the prompts to play.

## Game Rules

1. The game is played on a 3x3 grid.
2. The user can choose X or O as their marker.
3. The computer will automatically take turns after the user.
4. To make a move, enter the number corresponding to the position on the grid.
5. The positions are numbered from 1 to 9, as shown below:
6. The game ends when there is a winner or a tie.
7. A player wins if they have three markers in a row (horizontally, vertically, or diagonally).
8. If all positions on the grid are filled and there is no winner, it's a tie.

## Code Structure

The program is structured into several functions to handle different aspects of the game:

1. `display_board()`: Prints the current state of the Tic-Tac-Toe board.
2. `choose_markers()`: Allows the user to choose between X and O markers.
3. `handle_user_turn()`: Handles the user's turn by prompting for a position and updating the board.
4. `handle_computer_turn()`: Handles the computer's turn by randomly choosing an available position.
5. `check_game_over()`: Checks if the game is over by calling `check_winner()` and `check_tie()`.
6. `check_winner()`: Checks if there is a winner by calling `check_rows()`, `check_columns()`, and `check_diagonals()`.
7. `check_rows()`: Checks if any row has a winning combination of markers.
8. `check_columns()`: Checks if any column has a winning combination of markers.
9. `check_diagonals()`: Checks if any diagonal has a winning combination of markers.
10. `check_tie()`: Checks if the game is a tie.
11. `play_game()`: Starts the game by calling other functions in a loop.
