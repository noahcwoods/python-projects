print("Welcome to the rollercoaster!")
height = float(input("What is your height cm: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Please pay $5.00")
    elif age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("You cannot ride the rollercoaster!")

##############################################################

number = int(input("Enter an odd or even number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#############################################################

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25
additions = 0

if add_pepperoni == "Y":
    if size == "S":
        additions += 2
    else:
        additions += 3
if extra_cheese == "Y":
    additions += 1

if size == "S":
    print("Your final bill is: ${}.".format(SMALL_PIZZA + additions))
elif size == "M":
    print("Your final bill is: $ {}.".format(MEDIUM_PIZZA + additions))
else:
    print("Your final bill is: ${}.".format(LARGE_PIZZA + additions))


##############################################################

