import random

def rock_paper_scissors():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Game Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore: You {player_score} - {computer_score} Computer")
        
        # Player choice with input validation
        while True:
            player_choice = input("\nEnter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
            if player_choice in ['rock', 'paper', 'scissors', 'q']:
                break
            print("Invalid choice! Please try again.")
        
        if player_choice == 'q':
            break
            
        # Computer makes random choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'scissors' and computer_choice == 'paper') or
            (player_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
    
    # Final results
    print("\nFinal Score:")
    print(f"You {player_score} - {computer_score} Computer")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")
    
    print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
    rock_paper_scissors()