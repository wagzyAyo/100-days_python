import pandas
from datetime import datetime
import csv
import random
import glob

data_list = []
letters_list = []
text_files = glob.glob("./day32/letters/*.txt")


def birth_day_person(month, day, data):
    for person in data:
        if person.get("month") == str(month) and person.get("day") == str(day):
            return person.get('name')
    return None


with open("./day32/DOB.csv", mode="r", newline="") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data_list.append(row)


current_date = datetime.now().date()
current_month = current_date.month
current_day = current_date.day


celebrant = birth_day_person(current_month, current_day, data_list)


for lett in text_files:
    with open(lett, mode="r", encoding="utf-8") as letter:
        read_lett = letter.read()
        letters_list.append(read_lett)

letter_of_choice = random.choice(letters_list)
converted_letter = letter_of_choice.replace("[NAME]", celebrant)
print(converted_letter)

# print(letter_of_choice)
# print(current_day)
# print(current_month)

# print(data_list)


# Example usage:
