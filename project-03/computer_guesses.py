import random

def computer_guesses():
    print("\nWelcome to Guess the Number - Computer Edition!")
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    # Initialize game variables
    low = 1
    high = 100
    attempts = 0
    guessed_correctly = False

    # Game loop
    while not guessed_correctly:
        attempts += 1
        
        # Computer makes a guess (using binary search for efficiency)
        guess = (low + high) // 2
        print(f"\nMy guess #{attempts}: Is it {guess}?")

        # Get user feedback
        while True:
            feedback = input("(Enter 'H' if too high, 'L' if too low, 'C' if correct): ").upper()
            if feedback in ('H', 'L', 'C'):
                break
            print("Please enter H, L, or C!")

        # Process feedback
        if feedback == 'C':
            print(f"\nI guessed it in {attempts} attempts! 🎉")
            guessed_correctly = True
        elif feedback == 'H':
            high = guess - 1
            print("Okay, I'll guess lower next time!")
        else:  # 'L'
            low = guess + 1
            print("Okay, I'll guess higher next time!")

        # Check if user is cheating
        if low > high:
            print("\nHey! You must be changing your number! 😠")
            return

    # Play again option
    if input("\nWant to play again? (y/n): ").lower() == 'y':
        computer_guesses()
    else:
        print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
    computer_guesses()