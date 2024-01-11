import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# monday = data[data.day == "Monday"]
# converted_temp = monday.temp[0] * (9/5) + 32
#
# print(converted_temp)

#data = pandas.DataFrame(data_dict)
#data.to_csv("filepath")


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
all_fur_colors = data["Primary Fur Color"]
grey_colors = all_fur_colors.value_counts()['Gray']
red_colors = all_fur_colors.value_counts()['Cinnamon']
black_colors = all_fur_colors.value_counts()['Black']

print(type(red_colors))


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_colors, red_colors, black_colors]
}

processed_data = pandas.DataFrame(data_dict)
processed_data.to_csv("Squirrel_Counts_By_Color.csv")

