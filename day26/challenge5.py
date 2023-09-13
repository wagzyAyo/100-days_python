weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednessday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
# temperature from celcius to fahrenheit
new_dict = {day: weather * 9/5 + 32 for (day, weather) in weather_c.items()}
print(new_dict)
