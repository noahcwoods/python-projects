import game_data
import art
import random


def start_game():
    print(art.logo)
    done = False
    score = 0

    while not done:

        # Gets the data sets to compare
        if score == 0:
            option_a = game_data.data[get_comparison()]
        else:
            option_a = option_b

        option_b = game_data.data[get_comparison()]
        while option_b == option_a:
            option_b = game_data.data[get_comparison()]

        # Prints options to the user to compare
        print(f"\n\nA: {option_a['name']}, "
              f"a {option_a['description']}, "
              f"from {option_a['country']}")
        print(art.vs)
        print(f"B: {option_b['name']}, "
              f"a {option_b['description']}, "
              f"from {option_b['country']}")

        guess = input("Option [a] or [b]: ").lower()
        print(f"{option_a['name']}'s follower count is {option_a['follower_count']}")
        print(f"{option_b['name']}'s follower count is {option_b['follower_count']}")

        # Check results
        if check_result(option_a['follower_count'], option_b['follower_count'], guess):
            score += 1
            print(f"\nCongratulations! Your score is now {score}")
        else:
            done = True
            print(f"\nSorry! That's incorrect! Your score was {score}!")


def get_comparison():
    """Provides a random data set index"""
    return random.randint(0, len(game_data.data) - 1)


def check_result(rating_a, rating_b, player_guess):
    """Checks if the player guess is correct or not"""
    if player_guess.lower() == "a":
        if rating_a > rating_b:
            return True
        else:
            return False
    else:
        if rating_b > rating_a:
            return True
        else:
            return False


start_game()
