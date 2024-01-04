############DEBUGGING PRACTICE#####################

# Describe Problem
# NW - Function meant to print when it hits 20 but originally it
# will never hit 20, changed the range to include 20
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#
# # Reproduce the Bug
# # NW - Original randint range was 1 - 6 causing out of bounds.
# # updated to 0 - 5 to match the actual indices
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
#
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# f string was not being used, but {age} was included in the string
# print line needed to be indented into the if statement
# input needed wrapped in int()
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# Print is Your Friend
# == sign was used instead of  on pages = line
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
#b_list.append line needed to be indented
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])