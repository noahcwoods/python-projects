print("Welcome to the tip calculator")

totalBill = float(input("Enter the total bill:  "))
numPeople = int(input("How many people to split the bill?  "))
tip = float(input("How much tip would you like to be. 10 | 12 | 15:  ")) / 100

tip = totalBill * tip
totalBill = tip + totalBill
totalBill = totalBill / numPeople

print("Each person should pay: $", totalBill)



