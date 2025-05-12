import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=15):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flagged = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.first_move = True
        self.generate_board()

    def generate_board(self):
        """Generate mines after first move to ensure first click is safe"""
        pass  # Will be generated after first move

    def place_mines(self, first_x, first_y):
        """Place mines randomly, avoiding the first clicked cell"""
        mines_placed = 0
        while mines_placed < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
            # Don't place mine on first click or where mines already exist
            if (x == first_x and y == first_y) or self.board[y][x] == -1:
                continue
                
            self.board[y][x] = -1  # -1 represents a mine
            mines_placed += 1
            
            # Update adjacent cells' numbers
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] != -1:
                        self.board[ny][nx] += 1

    def print_board(self, show_all=False):
        """Print the current board state"""
        print("\n  " + " ".join(str(i).rjust(2) for i in range(self.width)))
        for y in range(self.height):
            print(str(y).rjust(2), end=" ")
            for x in range(self.width):
                if show_all:
                    if self.board[y][x] == -1:
                        print("💣", end=" ")
                    else:
                        print(str(self.board[y][x]).rjust(2), end=" ")
                else:
                    if self.flagged[y][x]:
                        print("🚩", end=" ")
                    elif not self.revealed[y][x]:
                        print("■", end=" ")
                    else:
                        if self.board[y][x] == -1:
                            print("💥", end=" ")
                        elif self.board[y][x] == 0:
                            print(" ", end=" ")
                        else:
                            print(str(self.board[y][x]).rjust(2), end=" ")
            print()
        print()

    def reveal(self, x, y):
        """Reveal a cell, recursively reveal adjacent cells if empty"""
        if not (0 <= x < self.width and 0 <= y < self.height) or self.revealed[y][x] or self.flagged[y][x]:
            return
        
        if self.first_move:
            self.place_mines(x, y)
            self.first_move = False
            
        self.revealed[y][x] = True
        
        if self.board[y][x] == -1:  # Hit a mine
            self.game_over = True
            return
            
        if self.board[y][x] == 0:  # Empty cell, reveal adjacent
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    self.reveal(x + dx, y + dy)

    def toggle_flag(self, x, y):
        """Toggle flag on/off for a cell"""
        if not self.revealed[y][x]:
            self.flagged[y][x] = not self.flagged[y][x]

    def check_win(self):
        """Check if all non-mine cells are revealed"""
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1 and not self.revealed[y][x]:
                    return False
        return True

def play_game():
    print("=== MINESWEEPER ===")
    print("Commands:")
    print("  r x y - Reveal cell at (x,y)")
    print("  f x y - Toggle flag at (x,y)")
    print("  q - Quit game")
    
    width = int(input("Enter board width (default 10): ") or 10)
    height = int(input("Enter board height (default 10): ") or 10)
    mines = int(input(f"Enter number of mines (default 15, max {width*height//2}): ") or 15)
    mines = min(mines, width*height//2)  # Limit mines to half the cells
    
    game = Minesweeper(width, height, mines)
    
    while not game.game_over:
        game.print_board()
        
        if game.check_win():
            print("Congratulations! You won!")
            game.print_board(show_all=True)
            break
            
        cmd = input("> ").strip().lower().split()
        
        if not cmd:
            continue
            
        if cmd[0] == 'q':
            print("Quitting game...")
            return
            
        if len(cmd) != 3:
            print("Invalid command!")
            continue
            
        try:
            x = int(cmd[1])
            y = int(cmd[2])
        except ValueError:
            print("Invalid coordinates!")
            continue
            
        if cmd[0] == 'r':
            game.reveal(x, y)
            if game.game_over:
                print("BOOM! You hit a mine! Game over.")
                game.print_board(show_all=True)
        elif cmd[0] == 'f':
            game.toggle_flag(x, y)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    while True:
        play_game()
        if input("Play again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break