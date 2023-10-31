# Define the board as a 3x3 grid
SET board = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]

#Create a function to determine who is the first player
FUNCTION choose_first_player()
	DISPLAY “Enter 1 to be the first player, Enter 2 to be the second”
	READ user_choice from the keyboard
	IF user_choice is 1
		RETURN “user”
	ELSE 
		RETURN “computer”
	END IF
END FUNCTION

#Create a function to determine what is the player’s symbol
FUNCTION get_user_symbol()
	DISPLAY “Do you want to be X or O”
	READ user_choice from the keyboard
	IF user_choice is “x”
		RETURN “x”
	ELSE 
		RETURN “o”
	END IF
END FUNCTION

# Create a function to display the Tic-Tac-Toe board
FUNCTION display_board(board)
FOR row in board
DISPLAY row
	END FOR
END FUNCTION

# Create a function to check for a winner. Check rows, columns, and diagonals for a winning combination. If a winning combination is found, return True, else return False
FUNCTION check_winner(board, player)
	FOR row in board
		FOR column in board
			IF every symbol in one row, column or diagonal is the same
				RETURN True
				END FUNCTION
			ELSE RETURN False
			END IF
		END FOR
	END FOR
END FUNCTION

# Create a function to get the user's move. Prompt the user for input. Validate the input to ensure it's a valid move then update the board with the user's move
FUNCTION get_user_move():
	SET is_input_valid of type boolean
	DO
		READ user_move from the keyboard
		IF user_move is not a valid input
			ASSIGN is_input_valid False
		ELSE 
			ASSIGN user_move into board
ASSIGN is_input_valid True
		END IF
	WHILE is_input_valid is False
	RETURN user_move
END FUNCTION		

# Create a function to get the computer's move
FUNCTION  get_computer_move():
	SET computer_move using an algorithm
	ASSIGN computer_move into board
	RETURN computer_move
END FUNCTION

# Create a function to save the game moves to a file. Open the "tictactoe.txt" file in append mode. Write the moves to the file
FUNCTION  save_moves_to_file(moves):
	OPEN tictactoe.txt file in append mode
	ASSIGN moves to tictactoe.txt
END FUNCTION

# Main game loop
FUNCTION  main():
SET player = choose_first_player()
SET user_symbol = get_user_symbol()
    	SET game_over = False

    	# Create an empty list to store the moves
    	SET moves of type array

# Loop until the game is over
# Display the board
DO 
display_board(board)
IF player is "user":
# Get the user's move
ASSIGN get_user_move() to user_move
            		ASSIGN user_move to moves[]
            		ASSIGN check_winner(board, user_symbol) to game_over 
ELSE
            		# Get the computer's move
            		ASSIGN get_computer_move() to computer_move
			ASSIGN computer_move to moves[]
            		ASSIGN check_winner(board, "o" IF user_symbol is "x" else "x") to game_over 
		END IF
        		# Switch the player for the next turn
        		player = "User" if player == "Computer" else "Computer"
WHILE game_over is false
# Display the final result and winner
display_board(board)
IF game_over is True
print("The winner is: " + player)
    
    	# Save the moves to a file
    	save_moves_to_file(moves)
END IF
END FUNCTION

# Call the main FUNCTION  to start the game
main()
