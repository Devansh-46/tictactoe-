# Tic-Tac-Toe Game

# Create an empty 3x3 grid
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the current state of the board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    print("Let's play Tic-Tac-Toe!")
    print_board()
    
    while True:
        # Get player input
        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))
        
        # Validate the input
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Print the updated board
        print_board()
        
        # Check if the current player has won
        if check_win(current_player):
            print(f"Player {current_player} wins!")
            break
        
        # Check if it's a tie
        if all(cell != ' ' for row in board for cell in row):
            print("It's a tie!")
            break
        
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
