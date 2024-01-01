import generate_word
import hangman_art

# Generate a word for hangman
generated_word = generate_word.generate()

# Game Controller
game_over = False
total_lives = 6
guessed_letters = []

# Visual display of '_' for the game
checked_word = []
for letter in generated_word:
    checked_word.append("_")

print(hangman_art.logo)
print("\n")

while not game_over:
    print(f"{' '.join(checked_word)}")
    print(f"\nYou have already guessed {guessed_letters}")
    print(f"You have {total_lives} lives remaining")
    user_guess = input("Guess a letter: ").lower()
    count = 0
    correct_guess = False

    if user_guess in guessed_letters:
        print("You already guessed that letter")
        continue
    else:
        guessed_letters.append(user_guess)


    for letter in generated_word:
        if letter == user_guess:
            checked_word[count] = user_guess
            correct_guess = True
        count += 1

    if not correct_guess:
        total_lives -= 1

    if total_lives == 0:
        game_over = True
        print("Sorry! You killed him you monster!")
        print(f"The word was {generated_word}")

    if "_" not in checked_word:
        game_over = True
        print("Congratulations! You Win!")

    print(hangman_art.stages[total_lives])
