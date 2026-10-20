import random

def hangman_game():
    words = ["python", "java", "javascript", "html", "css"]
    word = random.choice(words)
    guessed_letters = []
    wrong_attempts = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You have", max_wrong, "incorrect guesses allowed.\n")

    while wrong_attempts < max_wrong:
        # Display current word state
        display = []
        for letter in word:
            if letter in guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        print(" ".join(display))

        # Check if player has won
        if "_" not in display:
            print("\nCongratulations! You've won!")
            return

        # Get player guess
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in word:
            print("Correct!")
        else:
            wrong_attempts += 1
            print(f"Wrong guess! You have {max_wrong - wrong_attempts} attempts left.")

    # If loop ends, player has lost
    print("\nSorry, you've lost!")
    print("The word was:", word)

# Start the game
if __name__ == "__main__":
    hangman_game()