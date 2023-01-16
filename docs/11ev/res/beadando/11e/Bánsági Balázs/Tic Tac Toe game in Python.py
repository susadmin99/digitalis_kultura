# Tic Tac Toe game in Python

board = [" "," "," "," "," "," "," "," "," "]

def display_board():
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("   |   |")
    print("---|---|---")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("   |   |")
    print("---|---|---")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("   |   |")

def play_game():
    display_board()
    while True:
        handle_turn("X")
        check_for_game_over()
        handle_turn("O")
        check_for_game_over()

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == " ":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player
    display_board()

def check_for_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board