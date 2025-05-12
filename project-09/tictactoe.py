def print_board(board):
    """Prints the game board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    """Checks if there's a winner"""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    return None

def is_board_full(board):
    """Checks if the board is full"""
    return " " not in board

def get_player_move(board, player):
    """Gets valid player move"""
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1-9!")

def play_game():
    """Main game function"""
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9 from top-left to bottom-right")
    print_board([str(i+1) for i in range(9)])
    
    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            return winner
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            return None
        
        current_player = "O" if current_player == "X" else "X"

def main():
    """Main program loop"""
    while True:
        play_game()
        if input("Play again? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()