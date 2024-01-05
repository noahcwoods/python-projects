MENU = {
    "e": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = [
    {
        "name": "quarter",
        "value": .25,
        "provided": 0
    },
    {
        "name": "dime",
        "value": .10,
        "provided": 0
    },
    {
        "name": "nickel",
        "value": .05,
        "provided": 0
    },
    {
        "name": "penny",
        "value": .01,
        "provided": 0
    },
]


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")


def brew_coffee(type_of_coffee):
    water_needed = MENU[type_of_coffee]["ingredients"]["water"]
    milk_needed = MENU[type_of_coffee]["ingredients"]["milk"]
    coffee_needed = MENU[type_of_coffee]["ingredients"]["coffee"]
    resources["water"] -= water_needed
    resources["milk"] -= milk_needed
    resources["coffee"] -= coffee_needed


def check_resources(type_of_coffee):
    water_needed = MENU[type_of_coffee]["ingredients"]["water"]
    milk_needed = MENU[type_of_coffee]["ingredients"]["milk"]
    coffee_needed = MENU[type_of_coffee]["ingredients"]["coffee"]

    if resources["water"] - water_needed < 0:
        return (f"Sorry, there is not enough water for this. "
                f"\nCurrent water: {resources['water']}")
    elif resources["milk"] - milk_needed < 0:
        return (f"Sorry, there is not enough milk for this. "
                f"\nCurrent milk: {resources['milk']}")
    elif resources["coffee"] - coffee_needed < 0:
        return (f"Sorry, there is not enough coffee for this. "
                f"\nCurrent coffee: {resources['coffee']}")
    else:
        return "true"


def handle_payment(coins, type_of_coffee):
    cost = MENU[type_of_coffee]["cost"]
    provided_funds = 0

    for coin in coins:
        provided_funds += coin["value"] * coin["provided"]

    return provided_funds - cost


def clear_change():
    provided_quarters = 0
    provided_dimes = 0
    provided_nickels = 0
    provided_pennies = 0


def main():
    user_choice = input("What would you like? [e]spresso, [l]atte, [c]appuccino: ")

    while user_choice == "report":
        report()
        user_choice = input("What would you like? [e]spresso, [l]atte, [c]appuccino: ")



    coins[0]["provided"] += int(input("How many quarters? "))
    coins[1]["provided"] += int(input("How many dimes? "))
    coins[2]["provided"] += int(input("How many nickels? "))
    coins[3]["provided"] += int(input("How many pennies? "))

    if handle_payment(coins, user_choice) > 0:
        if check_resources(user_choice) == "true":
            brew_coffee(user_choice)
            print(f"Thank you! your change is {handle_payment(coins, user_choice)}")
            resources["money"] += MENU[user_choice]["cost"]
        else:
            print(check_resources(user_choice))

    else:
        clear_change()
        print("Sorry, you don't have enough. We have issued a refund of your change.")


done = False
while not done:
    main()
