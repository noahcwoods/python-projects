# List/Dict Comprehension  - Applied to Day 25
import csv

# import random
#
# names = ["beth", "john", "noah", "alicia", "tom"]
#
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for student, score in student_scores.items() if score >= 70}
# print(passed_students)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# new_dict = {}


with open("nato_phonetic_alphabet.csv") as f:
    reader = csv.reader(f)
    new_dict = dict(reader)
    print(new_dict)

completed = False
while not completed:

    user_word = input("Enter a word to convert: ")
    result = []

    for letter in user_word:
        try:
            result.append(new_dict[letter.upper()])
        except KeyError:
            print("Only letters in the alphabet please, try again...")
            result = []
            completed = False
            break
        else:
            completed = True

print(result)