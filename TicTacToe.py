import random

# BOARD DEFINITION
def display_board(board):
    print("  |   |")
    print(board[1] + " | "+ board[2] + " | " + board[3])
    print("  |   |")
    print("----------")
    print("  |   |")
    print(board[4] + " | "+ board[5] + " | " + board[6])
    print("  |   |")
    print("----------")
    print("  |   |")
    print(board[7] + " | "+ board[8] + " | " + board[9])
    print("  |   |")

# CHOOSING A MARKER
def player_input():
    player2 = ''
    players = []
    condition = False

    while condition == False:
        player1 = input(" Player 1 - Please pick a marker 'X' or 'O'").upper()

        if player1.lower() in ["x", "o"]:
            if player1.lower() == "x":
                player2 = "O"
            else:
                player2 = "X"

            condition = True
        else:
            print("Please choose X or O")

    players = [player1, player2]
    print("Player1:" + players[0] + "\n" + "Player2:" + players[1])
    return players

# FUNCTION TO PLACE A MARKER :)
def place_marker(board, marker, position):
    board[position] = marker

# FUNC TO CHECK EVERY POSSIBLE WINNING COMBINATION
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

#RANDOMLY CHOOSING WHO STARTS THE GAME
def choose_first():
    first = random.randint(0,1)
    print("First move is for Player"+str(first+1))
    return first

# FUNC TO CHECK IF THE CHOOSEN PLACE IS FREE
def space_check(board, position):
    if board[position] == "X" or board[position] == "O" :
        return False
    else:
        return True

# CHECKING IF THE BOARD IS FULL
def full_board_check(board):
    board_counter = 0
    for i in range(1,10):
        if board[i] == "X" or board[i] == "O":
            board_counter += 1
    if board_counter < 9:
        return False
    else:
        return True

# WHOLE FUNC COMBINING PICKING THE PLACE TO PUT A MARKER BY A PLAYER AND CHECKING IF IT'S FREE
def player_choice(board):
    flag_choice = False
    print("It's " + board[0] + " turn\n")
    while flag_choice == False:
        position_new = input("Please choose another position on the board: ")
        if position_new.isdigit() == False:
            print("Please provide a position by number from 1 to 9")
        else:
            if int(position_new) not in range(1, 10):
                print("Please choose the postion from 1 to 9:")
                continue
            else:
                if space_check(board, int(position_new)) == True:
                    flag_choice = True
                else:
                    print("It's taken")
                    continue

    return int(position_new)

# FUNC TO CHECK IF THE PLAYER WANTS TO PLAY AGAIN
def replay():
    flag_replay = False
    while flag_replay == False:
        answer = input("Do you want to play again?[YES / NO]:").upper()
        if answer != "NO" and answer != "YES":
            print("Do you want to play again? Please write YES or NO:")
        else:
            if answer.upper() == "YES":
                flag_replay = True
                return True

            else:
                flag_replay = True
                return False

#    GAME BEGINS ************
while True:
    print('Welcome to Tic Tac Toe!')
    # contidions for start:
    players = player_input()
    first = choose_first()
    board = [players[first], '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        place_marker(board, board[0], player_choice(board))
        display_board(board)
        if win_check(board, board[0]) == True:
            print("BRAWO! Player " + board[0] + " has won! :)")
            break
        elif full_board_check(board) == True:
            print("Board is full! This time nobody won :)")
            break

        if board[0] == "X":
            print("zmiana na o")
            board[0] = "O"
        elif board[0] == "O":
            print("zmiana na x")
            board[0] = "X"

    if replay() == False:
        break
