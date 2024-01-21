
# File not found
# with open("a_file.txt") as file:
#     print(file.read())

# Key error
# a_dict = {"key", "value"}
# value = a_dict["non-existent key"]

# Index error
# fruit_list = ["apple", "banana", "orange"]
# fruit = fruit_list[3]

# Type error
# text = "abc"
# text = text + 5

# try:
#     file = open("a_file.txt")
# except FileNotFoundError as err:
#     print(err)
#     print("Creating File now!")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise KeyError("This error has nothing to do with this example :)")

# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Height is greater than maximum human height")
#
# bmi = weight / height ** 2
# print(bmi)

