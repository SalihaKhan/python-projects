def validate_board(board):
    """Validates that a Sudoku board is properly formatted and has valid numbers."""
    if len(board) != 9:
        return False
    
    for row in board:
        if len(row) != 9:
            return False
        for num in row:
            if not isinstance(num, int) or num < 0 or num > 9:
                return False
                
    return True

def is_complete(board):
    """Checks if the board is completely filled with valid numbers."""
    for row in board:
        for num in row:
            if num == 0 or num > 9:
                return False
    return True