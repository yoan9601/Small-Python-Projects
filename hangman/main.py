# Hangman Game
# Classic word guessing game with ASCII art and lives system
# Author: yoan9601

import random
import hangman_art
import hangman_words

# Game setup
print(hangman_art.logo)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
game_over = False
correct_letters = []

# Create placeholder
display = ["_" for _ in range(word_length)]
print(f"Word to guess: {' '.join(display)}")

while not game_over:
    print(f"\n{'*' * 25} {lives}/6 LIVES LEFT {'*' * 25}")
    
    guess = input("\nGuess a letter: ").lower()

    # Already guessed
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try another letter!")
        continue
    
    # Correct guess
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        correct_letters.append(guess)
    # Wrong guess
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life!")
    
    print(f"\nWord: {' '.join(display)}")
    print(hangman_art.stages[lives])

    # Check win/lose
    if "_" not in display:
        game_over = True
        print("\n" + "*" * 60)
        print("CONGRATULATIONS! YOU WIN!")
        print("*" * 60)
    elif lives == 0:
        game_over = True
        print("\n" + "*" * 60)
        print(f"GAME OVER! The word was: {chosen_word.upper()}")
        print("*" * 60)
