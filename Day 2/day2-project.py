print("Welcome to the tip calculator")

totalBill = input("Enter the total bill:  ")
numPeople = input("How many people to split the bill?  ")
tip = float(input("How much tip would you like to be. 10 | 12 | 15:  ")) / 100

tip = float(totalBill) * float(tip)
totalBill = float(tip) + float(totalBill)
totalBill = totalBill / float(numPeople)

print("Each person should pay: $", totalBill)



