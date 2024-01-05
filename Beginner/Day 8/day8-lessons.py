def prime_checker(number):
    counting_numbers = []
    for i in range(2, number - 1):
        counting_numbers.append(i)
    prime_number = True
    for num in counting_numbers:
        if number % num == 0:
            print("It's not a prime number.")
            prime_number = False
            break
    if prime_number is True:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("enter your number: "))  # Check this number
prime_checker(number=n)