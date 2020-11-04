# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
        
# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"

def display_board():
    print(f"""{board[0]} | {board[1]} | {board[2]}   1 | 2 | 3 
{board[3]} | {board[4]} | {board[5]}   4 | 5 | 6
{board[6]} | {board[7]} | {board[8]}   7 | 8 | 9""")

def play_game():
    display_board()

    while game_still_going:
        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    else:
        print("Tie")

def handle_turn(player):
    print(player+" turn.")
    position = input("Choose a position from 1-9: ")

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    global winner
    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
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
    #set up global varibales
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    else:
        return None

def check_columns():
    #set up global varibales
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    else:
        return None

def check_diagonals():
    #set up global varibales
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[3]
    else:
        return None

def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

play_game()