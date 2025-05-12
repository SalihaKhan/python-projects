import random

def guess_the_number():
    print("\nWelcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Game setup
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining_guesses = max_attempts - attempts + 1
        
        # Get player's guess
        try:
            guess = int(input(f"\nGuess #{attempts} ({remaining_guesses} left): "))
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        # Check guess
        if guess < secret_number:
            print("Too low! Try higher.")
        elif guess > secret_number:
            print("Too high! Try lower.")
        else:
            print(f"\nCongratulations! You guessed it in {attempts} tries!")
            break
    
    # If player runs out of guesses
    if attempts == max_attempts and guess != secret_number:
        print(f"\nGame over! The number was {secret_number}.")
    
    # Play again option
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        guess_the_number()
    else:
        print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
    guess_the_number()