import random

NUMBER = random.randint(1, 100)


def difficulty_level():
    game_modes = {
        "e": 10,
        "h": 5,
    }
    difficulty = input("[e]asy or [h]ard: ")
    return game_modes[difficulty]


def guess():
    return int(input("Guess a number: "))


def compare(guess):
    if guess == NUMBER:
        return True
    elif guess < NUMBER:
        print("Higher!")
    elif guess > NUMBER:
        print("Lower!")


def start():
    global LIVES
    print(f"You have {LIVES} guesses to find the number!")
    while LIVES > 0:
        if not compare(guess()):
            LIVES -= 1
            print(f"You have {LIVES} guesses remaining\n")

        else:
            print("You Win!\n")
            break
    if LIVES == 0:
        print("You Lose!\n")

LIVES = difficulty_level()
print("\nWelcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.\n")
start()
