import random

# Define the board as a 3x3 grid
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Create a function to display the Tic-Tac-Toe board


def game_initialize():
    player = "User"
    user_symbol = input("Choose your symbol (X or O): ").upper()

    moves = []
    game_over = False


def display_board(board):
    for row in board:
        print(row)

# Create a function to check for a winner


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Create a function to get the user's move


# def get_user_move():

# Create a function to get the computer's move


# def get_computer_move():

# Create a function to save the game moves to a file


# def save_moves_to_file(moves):

# Main game loop


def main():
    game_initialize()

    while not game_over:
        display_board(board)
        if player == "User":
            user_move = get_user_move()
            moves.append(user_move)
            board[user_move[0]][user_move[1]] = user_symbol
            game_over = check_winner(board, user_symbol)
        else:
            computer_move = get_computer_move()
            moves.append(computer_move)
            board[computer_move[0]][computer_move[1]
                                    ] = "O" if user_symbol == "X" else "X"
            game_over = check_winner(board, "O" if user_symbol == "X" else "X")

        player = "User" if player == "Computer" else "Computer"

    display_board(board)
    if game_over:
        print("The winner is: " + player)

    # save_moves_to_file(moves)


# Call the main function to start the game
main()
