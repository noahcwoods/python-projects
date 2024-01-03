enemies = 1


# Avoid modifying global scope. It can be messy.
def increase_enemies():
    # global enemies
    # print(f"enemies: {enemies}")
    return enemies + 1


# increase_enemies()
enemies = increase_enemies()
print(f"enemies: {enemies}")

#Global Constant
PI = 3.14159
URL = "https://en.wikipedia.org/wiki"
TWITTER_HANDLE = "@noahcwoods"
TWITTER_NAME = "Noah Woods"
