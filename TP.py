import random

# Define the board as a 3x3 grid
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Create a function to display the Tic-Tac-Toe board


def display_board(board):
    for row in board:
        print(row)

# Create a function to check for a winner


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check main diagonal
    if all(board[i][i] == player for i in range(3)):
        return True

    # Check secondary diagonal
    if all(board[i][2-i] == player for i in range(3)):
        return True

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        return True

    return False

# Create a function to get the user's move


def get_user_move():
    while True:
        try:
            x = int(input('Please choose a row from 1 to 3: ')) - 1
            if x not in range(3):
                print('Invalid row number, please try again.')
                continue

            y = int(input('Please choose a column from 1 to 3: ')) - 1
            if y not in range(3):
                print('Invalid column number, please try again.')
                continue

            if board[x][y] != " ":
                print('Position already taken, please choose another position.')

            return x, y
        except ValueError:
            print('Please enter a number.')


# Create a function to get the computer's move


def get_computer_move():
    empty_cells = [(i, j) for i in range(3)
                   for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)


# Create a function to save the game moves to a file
SAVE_FILE = 'moves.txt'


def save_moves_to_file(moves):
    with open(SAVE_FILE, 'a+') as save_file:
        for move in moves:
            save_file.writelines(f"{move[0]}, {move[1]}\n")


# Main game loop

# Create a function to initialize the game
def initialize_game():
    while True:
        user_symbol = input("Choose your symbol (X or O): ").upper()
        if user_symbol in ['X', 'O']:
            break
        else:
            print("Invalid symbol. Please choose X or O.")
    player = "User"
    moves = []
    game_over = False
    return player, user_symbol, moves, game_over


def main():
    player, user_symbol, moves, game_over = initialize_game()
    display_board(board)

    while not game_over:

        if player == "User":
            user_move = get_user_move()
            moves.append(user_move)
            board[user_move[0]][user_move[1]] = user_symbol
            game_over = check_winner(board, user_symbol)
            if game_over:
                break
        else:
            opponent_symbol = "O" if user_symbol == "X" else "X"
            computer_move = get_computer_move()
            moves.append(computer_move)
            board[computer_move[0]][computer_move[1]] = opponent_symbol
            game_over = check_winner(board, opponent_symbol)
            display_board(board)
            if game_over:
                break

        player = "User" if player == "Computer" else "Computer"
    if game_over:
        print("The winner is: " + player)


# Call the main function to start the game
main()
