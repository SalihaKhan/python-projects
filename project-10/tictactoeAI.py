import random

def print_board(board):
    """Prints the game board with borders"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    """Checks if there's a winner"""
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    return None

def is_board_full(board):
    """Checks if the board is full"""
    return " " not in board

def get_human_move(board, player):
    """Gets valid human player move"""
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1-9!")

def get_ai_move(board, ai_player):
    """Unbeatable AI using minimax algorithm"""
    human_player = "X" if ai_player == "O" else "O"
    
    def minimax(board, depth, is_maximizing):
        winner = check_winner(board)
        if winner == ai_player:
            return 10 - depth
        elif winner == human_player:
            return depth - 10
        elif is_board_full(board):
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = ai_player
                    score = minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = human_player
                    score = minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score
    
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ai_player
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game(against_ai=True):
    """Main game function"""
    board = [" "] * 9
    current_player = "X"
    ai_player = "O" if against_ai else None
    
    print("\nWelcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9 from top-left to bottom-right")
    print_board([str(i+1) for i in range(9)])
    
    while True:
        print_board(board)
        
        if current_player == ai_player:
            print("AI is thinking...")
            move = get_ai_move(board, ai_player)
        else:
            move = get_human_move(board, current_player)
        
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == ai_player:
                print("AI wins! Better luck next time.")
            else:
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
        print("\n" + "="*30)
        print(" TIC-TAC-TOE ".center(30, "="))
        print("="*30)
        print("\n1. Play against AI")
        print("2. Two Player Mode")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ")
        
        if choice == "1":
            play_game(against_ai=True)
        elif choice == "2":
            play_game(against_ai=False)
        elif choice == "3":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice! Please enter 1-3.")
        
        if input("\nPlay again? (y/n): ").lower() != "y":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()