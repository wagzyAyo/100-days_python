#!/usr/bin/python3
import math
def paint_calc(height, width, coverage):
    heigth = int(height)
    width = int(width)
    coverage = int(coverage)
    result = (height * width) / coverage
    result = math.floor(result)
    print(f"You will need {result} cans of paint")

paint_calc(3, 9, 5)
