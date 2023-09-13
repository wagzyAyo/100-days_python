# with open("./day25/weather-data.csv") as file:
#    print(file.readlines())

import csv
import pandas

# with open("./day25/weather-data.csv") as file:
#    data = csv.reader(file)
#    temp = []
#    for columns in data:
#        columns[1:-1]
#        for row in data:
#            temperature = row[1]
#            temp.append(int(temperature))
#    print(temp)

# data = pandas.read_csv("./day25/weather-data.csv")

# data_list = data["temp"].to_list()


# average = sum(data_list) / len(data_list)

# data_max = data["temp"].max()
# print(data_max)

# print(data[data["day"] == "Monday"])

# Get the day with highesttemperature

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)

data = pandas.read_csv(
    "./day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Squirrel_count": [gray_fur_count, cinnamon_fur_count, black_fur_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./day25/Squirell_count.csv")
