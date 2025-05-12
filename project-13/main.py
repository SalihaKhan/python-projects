from solver import solve_sudoku
from validator import validate_board, is_complete
from utils import print_board, load_puzzle
import time

def main():
    print("Sudoku Solver")
    print("-------------")
    
    # Load puzzle (you can modify this to accept user input)
    puzzle_file = "puzzles/medium.txt"
    board = load_puzzle(puzzle_file)
    
    if not board or not validate_board(board):
        print("Invalid puzzle!")
        return
    
    print("\nUnsolved Puzzle:")
    print_board(board)
    
    print("\nSolving...")
    start_time = time.time()
    
    if solve_sudoku(board):
        end_time = time.time()
        print("\nSolved Puzzle:")
        print_board(board)
        print(f"\nTime taken: {end_time - start_time:.2f} seconds")
        
        if is_complete(board):
            print("Solution is complete and valid!")
        else:
            print("Warning: Solution might be incomplete or invalid!")
    else:
        print("\nNo solution exists for this puzzle!")

if __name__ == "__main__":
    main()