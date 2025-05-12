import datetime
import os

def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please provide the following words:")
    
    # Get user inputs
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    plural_noun = input("Plural noun: ")
    game = input("Game: ")
    plural_noun2 = input("Plural noun: ")
    verb_ing1 = input("Verb ending in -ing: ")
    verb_ing2 = input("Verb ending in -ing: ")
    plural_noun3 = input("Plural noun: ")
    verb_ing3 = input("Verb ending in -ing: ")
    noun3 = input("Noun: ")
    plant = input("Plant: ")
    body_part = input("Part of the body: ")
    place = input("A place: ")
    verb_ing4 = input("Verb ending in -ing: ")
    adjective3 = input("Adjective: ")
    number = input("Number: ")
    plural_noun4 = input("Plural noun: ")
    
    # The Mad Lib story template
    story = f"""
    A vacation is when you take a trip to some {adjective1} place
    with your {adjective2} family. Usually you go to some place
    that is near a/an {noun1} or up on a/an {noun2}.
    A good vacation place is one where you can ride {plural_noun}
    or play {game} or go hunting for {plural_noun2}. I like
    to spend my time {verb_ing1} or {verb_ing2}.
    When parents go on a vacation, they spend their time eating
    three {plural_noun3} a day, and fathers play golf, and mothers
    sit around {verb_ing3}. Last summer, my little brother
    fell in a/an {noun3} and got poison {plant} all
    over his {body_part}. My family is going to go to (the)
    {place}, and I will practice {verb_ing4}. Parents
    need vacations more than kids because parents are always very
    {adjective3} and because they have to work {number}
    hours every day all year making enough {plural_noun4} to pay
    for the vacation.
    """
    
    print("\nHere's your Mad Lib story:")
    print(story)
    
    # Ask if user wants to save the story
    save_choice = input("\nWould you like to save this story? (yes/no): ").lower()
    if save_choice == 'yes':
        save_story(story)

def save_story(story):
    """Save the generated story to a file with a timestamp"""
    # Create a directory for stories if it doesn't exist
    if not os.path.exists('mad_libs_stories'):
        os.makedirs('mad_libs_stories')
    
    # Generate a filename with current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"mad_libs_stories/story_{timestamp}.txt"
    
    # Save the story to file
    with open(filename, 'w') as file:
        file.write(story)
    
    print(f"Story saved as {filename}")

def view_saved_stories():
    """Display a list of all saved stories"""
    if not os.path.exists('mad_libs_stories'):
        print("No stories have been saved yet.")
        return
    
    print("\nSaved Stories:")
    stories = os.listdir('mad_libs_stories')
    for i, story in enumerate(stories, 1):
        print(f"{i}. {story}")
    
    # Option to view a specific story
    choice = input("\nEnter number to view a story (or '0' to go back): ")
    if choice != '0':
        try:
            selected_story = stories[int(choice)-1]
            with open(f'mad_libs_stories/{selected_story}', 'r') as file:
                print("\n" + file.read())
        except (IndexError, ValueError):
            print("Invalid selection.")

def main_menu():
    while True:
        print("\n=== Mad Libs Main Menu ===")
        print("1. Create a new Mad Lib")
        print("2. View saved stories")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            mad_libs()
        elif choice == '2':
            view_saved_stories()
        elif choice == '3':
            print("Thanks for playing Mad Libs!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()