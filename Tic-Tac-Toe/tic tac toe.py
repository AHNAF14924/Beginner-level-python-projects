import random
board = [' ' for _ in range(9)]
user_marker = ''
computer_marker = ''
game_still_on = True
winner = None


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def choose_markers():
    global user_marker, computer_marker
    user_marker = input("Choose X or O: ").upper()
    while user_marker != 'X' and user_marker != 'O':
        user_marker = input("Invalid input. Choose X or O: ").upper()

    if user_marker == 'X':
        computer_marker = 'O'
    else:
        computer_marker = 'X'


def handle_user_turn():
    print("User's turn.")
    position = input("Choose a position from 1-9: ")

    valid_position = False
    while not valid_position:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == ' ':
            valid_position = True
        else:
            print("That position is already filled. Choose another position: ")

    board[position] = user_marker
    display_board()


def handle_computer_turn():
    print("Computer's turn.")
    position = random.randint(0, 8)
    while board[position] != ' ':
        position = random.randint(0, 8)

    board[position] = computer_marker
    display_board()


def check_game_over():
    check_winner()
    check_tie()


def check_winner():
    global game_still_on

    rows_winner = check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()

    if rows_winner:
        game_still_on = False
    elif columns_winner:
        game_still_on = False
    elif diagonals_winner:
        game_still_on = False

    if rows_winner:
        print(rows_winner, "wins!")
    elif columns_winner:
        print(columns_winner, "wins!")
    elif diagonals_winner:
        print(diagonals_winner, "wins!")


def check_rows():
    global game_still_on

    row1 = board[0] == board[1] == board[2] != ' '
    row2 = board[3] == board[4] == board[5] != ' '
    row3 = board[6] == board[7] == board[8] != ' '

    if row1 or row2 or row3:
        game_still_on = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    return None


def check_columns():
    global game_still_on

    column1 = board[0] == board[3] == board[6] != ' '
    column2 = board[1] == board[4] == board[7] != ' '
    column3 = board[2] == board[5] == board[8] != ' '

    if column1 or column2 or column3:
        game_still_on = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

    return None


def check_diagonals():
    global game_still_on

    diagonal1 = board[0] == board[4] == board[8] != ' '
    diagonal2 = board[2] == board[4] == board[6] != ' '

    if diagonal1 or diagonal2:
        game_still_on = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]

    return None


def check_tie():
    global game_still_on

    if ' ' not in board:
        game_still_on = False
        print("It's a tie!")


def play_game():
    display_board()
    choose_markers()

    while game_still_on:
        handle_user_turn()
        check_game_over()

        if not game_still_on:
            break

        handle_computer_turn()
        check_game_over()


if __name__ == '__main__':
    play_game()
