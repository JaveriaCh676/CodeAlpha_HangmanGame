import random

# List of predefined words
words = ["apple", "mango", "grape", "melon", "peach"]

# Randomly choose a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses > 0:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check input validity
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses -= 1
        print("❌ Wrong Guess!")
        print("Remaining chances:", wrong_guesses)

# If player loses
if wrong_guesses == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)