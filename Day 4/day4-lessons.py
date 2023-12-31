import random
import demo_module

randomInt = random.randint(0,2)
print(randomInt)
print(demo_module.pi)

randomFloat = random.random()
print(randomFloat)

love_score = random.randint(1,100)
print(f"The love score is {love_score}")

names = ["Pennsylvania", "New York", "Florida", "Massachusetts"]

print(names[-1])
print(names[0])

names[0] = "Pencilvania"
print(names[0])

names.append("Noah Woods")
print(names[-1])

names.extend(["Cole", "Taylor", "Alicia"])
print(names)

testString = "Cole223"
print(testString.count("2"))

def userGuess():
    guess = int(input(""))
    
