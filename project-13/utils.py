def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def load_puzzle(filename):
    """Loads a Sudoku puzzle from a text file."""
    try:
        with open(filename, 'r') as f:
            board = []
            for line in f:
                row = [int(num) for num in line.strip().split()]
                board.append(row)
            return board
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ValueError:
        print("Error: Puzzle file contains invalid characters.")
        return None