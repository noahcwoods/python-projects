import random

choice = input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors: ")
computerChoice = random.randint(0,2)

print(f"Computer choice: {computerChoice}")
print(f"Your choice: {choice}")


if int(choice) == computerChoice:
    print("Draw")
elif choice == "1":
    if computerChoice == 0:
        print("You Win!")
    else:
        print("You Lose!")
elif choice == "2":
    if computerChoice == 1:
        print("You Win!")
    else:
        print("You Lose!")
else:
    if computerChoice == 2:
        print("You Win!")
    else:
        print("You Lose!")