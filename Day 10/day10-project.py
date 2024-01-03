import art


def addition(first_num, second_num):
    """Adds two numbers"""
    return first_num + second_num


def subtraction(first_num, second_num):
    """Subtracts two numbers"""
    return first_num - second_num


def multiplication(first_num, second_num):
    """Multiplies two numbers"""
    return first_num * second_num


def division(first_num, second_num):
    """Divides two numbers"""
    return first_num / second_num


print(art.logo)
print("Welcome to Python Calculator")

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    """Calculates"""
    done = False
    first_num = float(input("Please enter a number: "))
    while not done:

        operand = input('Please enter an operand: (*, /, +, -): ')

        second_num = float(input("Please enter another number: "))
        result = operations[operand](first_num, second_num)
        print(f"{first_num} {operand} {second_num} = {result}")

        checker = input("\n\nUse old value [o]\nUse new value [n]\nStop the program [q]\n: ")

        if checker == "q":
            done = True
        elif checker == "o":
            first_num = result
        else:
            calculator()

        print("\n\n\n")


calculator()
