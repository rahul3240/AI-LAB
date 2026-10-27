board = [" " for _ in range(9)]

HUMAN = "X"
COMPUTER = "O"


def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("--+---+--")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def is_full():
    return " " not in board


def utility():
    if check_winner(COMPUTER):
        return 1
    elif check_winner(HUMAN):
        return -1
    else:
        return 0


def minimax(is_maximizing):
    
    if check_winner(COMPUTER):
        return 1

    if check_winner(HUMAN):
        return -1

    if is_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = COMPUTER

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":

            board[i] = COMPUTER

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():
    print("TIC-TAC-TOE using MINIMAX")
    print("Human: X")
    print("Computer: O")

    display_board()

    while True:

        while True:
            try:
                row, col = map(
                    int,
                    input("Enter row and column (1-3): ").split()
                )

                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("Invalid position! Enter values from 1 to 3.")
                    continue

                position = (row - 1) * 3 + (col - 1)

                if board[position] != " ":
                    print("Position already occupied! Try again.")
                    continue

                break

            except ValueError:
                print("Enter two numbers separated by space.")

        board[position] = HUMAN

        display_board()

        if check_winner(HUMAN):
            print("Human Player Wins")
            break

        if is_full():
            print("Game Draw")
            break
        
        move = best_move()
        board[move] = COMPUTER

        display_board()

        if check_winner(COMPUTER):
            print("Computer Wins")
            break

        if is_full():
            print("Game Draw")
            break


play_game()