programming_dict = {
    "Bug": "An error in the program",
    "Function": "A peice of code that you can easily call over and over",
    "Loop": "The action of doing something over and over again",
}

print(programming_dict["Bug"])

programming_dict["New Loop"] = "The action of doing something even more over and over"
print(programming_dict)

empty_dict = {}

#programming_dict.clear()
print(programming_dict)

for key, value in programming_dict.items():
    print(f"{key}: {value}")

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list / nesting a dictionary
travel_log = {
    "France": [
        "Paris",
        "Lille",
        "Dijon",
    ],
}

travel_log2 = {
    "France": {
        "cities_visited": [
            "Paris",
            "Lille",
            "Dijon",
        ],
        "total_visits": 12,
    },
    "United States": {
        "cities_visited": [
            "State College",
            "Pittsburgh",
            "Altoona",
        ],
        "total_visits": 576,
        "ratings": {
            "State College": 5.5,
            "Pittsburgh": 9.5,
            "Altoona": 3.2,
        },
    },
}

# Nesting a dict inside a list

list1 = [
    {
        "country": "France",
        "cities_visited": ["Paris, Lille, Dijon"],
        "total_visits": 12
    }
]

