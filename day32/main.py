import pandas
from datetime import datetime
import random


file = pandas.read_csv("./day32/DOB.csv")

print(file["name"])
