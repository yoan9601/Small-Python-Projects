"""
Guess the Number Game
A simple number guessing game with difficulty levels.

Author: Yoan Boyadzhiev
Date: November 2025
"""

import random
from logo import LOGO


def display_welcome():
    """Display welcome message with ASCII art."""
    print(LOGO)
    print("\n" + "="*55)
    print("         Welcome! I'm thinking of a number.")
    print("            Can you guess what it is?")
    print("="*55 + "\n")


def choose_difficulty():
    """
    Let the player choose difficulty level.
    Returns: tuple (max_number, max_attempts, difficulty_name)
    """
    print("Choose your difficulty level:\n")
    print("1. EASY   - Number between 1-50  (10 attempts)")
    print("2. MEDIUM - Number between 1-100 (7 attempts)")
    print("3. HARD   - Number between 1-200 (5 attempts)")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            return 50, 10, "EASY"
        elif choice == '2':
            return 100, 7, "MEDIUM"
        elif choice == '3':
            return 200, 5, "HARD"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def get_guess(max_num):
    """
    Get a valid number guess from the user.
    Args:
        max_num: maximum valid number
    Returns: integer guess
    """
    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_num}): "))
            if 1 <= guess <= max_num:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_num}!")
        except ValueError:
            print("That's not a valid number! Try again.")


def give_hint(guess, target):
    """
    Provide hint based on the guess.
    Args:
        guess: player's guess
        target: the target number
    """
    if guess < target:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")


def play_game():
    """
    Main game logic.
    Returns: boolean (True if player wants to play again)
    """
    # Choose difficulty
    max_num, max_attempts, difficulty = choose_difficulty()
    
    # Generate random number
    target_number = random.randint(1, max_num)
    attempts_used = 0
    
    print(f"\n{'='*50}")
    print(f"Difficulty: {difficulty}")
    print(f"I'm thinking of a number between 1 and {max_num}")
    print(f"You have {max_attempts} attempts to guess it!")
    print(f"{'='*50}\n")
    
    # Game loop
    while attempts_used < max_attempts:
        guess = get_guess(max_num)
        attempts_used += 1
        
        # Check if guess is correct
        if guess == target_number:
            print("\n" + "="*50)
            print("CONGRATULATIONS! YOU WIN!")
            print(f"You guessed the number: {target_number}")
            print(f"It took you {attempts_used} attempt(s)!")
            print("="*50 + "\n")
            return ask_play_again()
        
        # Wrong guess - give hint
        attempts_left = max_attempts - attempts_used
        give_hint(guess, target_number)
        
        if attempts_left > 0:
            print(f"Attempts remaining: {attempts_left}\n")
    
    # Player ran out of attempts
    print("\n" + "="*50)
    print("GAME OVER!")
    print(f"You've used all {max_attempts} attempts.")
    print(f"The number was: {target_number}")
    print("Better luck next time!")
    print("="*50 + "\n")
    
    return ask_play_again()


def ask_play_again():
    """
    Ask if player wants to play again.
    Returns: boolean
    """
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please answer 'yes' or 'no'")


def main():
    """Main function to run the game."""
    display_welcome()
    
    # Game loop
    playing = True
    while playing:
        playing = play_game()
    
    # Goodbye message
    print("\n" + "="*50)
    print("Thanks for playing Guess the Number!")
    print("See you next time!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
