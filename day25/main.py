# with open("./day25/weather-data.csv") as file:
#    print(file.readlines())

import csv


with open("./day25/weather-data.csv") as file:
    data = csv.reader(file)
    temp = []
    for columns in data:
        columns[1:-1]
        for row in data:
            temperature = row[1]
            temp.append(int(temperature))
    print(temp)
