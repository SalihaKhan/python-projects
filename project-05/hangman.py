import random

def hangman():
    # Word bank
    words = ["python", "programming", "hangman", "computer", "keyboard", 
             "developer", "algorithm", "variable", "function", "dictionary"]
    
    # Select random word
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Head, body, 2 arms, 2 legs
    word_progress = ["_"] * len(secret_word)
    
    # Hangman ASCII art stages
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("You have 6 attempts before the man is hanged!")
    
    while attempts > 0 and "_" in word_progress:
        # Display current game state
        print(hangman_stages[6 - attempts])
        print(" ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        
        # Get player's guess
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed that letter!")
                else:
                    break
            else:
                print("Please enter a single letter!")
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("Correct!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_progress[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
    
    # Game over message
    print(hangman_stages[6 - attempts])  # Show final hangman state
    if "_" not in word_progress:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game over! The word was: {secret_word}")
    
    # Play again option
    if input("\nPlay again? (y/n): ").lower() == 'y':
        hangman()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    hangman()