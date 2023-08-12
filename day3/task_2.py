small = 15
medium = 20
large = 25
total = 0
order = input(
    "Hello,welcome to pizza nation\nPlace your order in size S M L: ")
pep = input("Include peperoni? Y or N: ")
Cheese = input("Include extra Cheese? Y or N: ")
# small
if order == "S":
    total += small
    if pep == "Y":
        total += 2
    if Cheese == "Y":
        total += 1
# Medium
elif order == "M":
    total += medium
    if pep == "Y":
        total += 3
    if Cheese == "Y":
        total += 1
# large
elif order == "L":
    total += large
    if pep == "Y":
        total += 3
    if Cheese == "Y":
        total += 1
else:
    print("choose from the menu Small Medium or Large")
print(f"Your total bill is ${total}.00")
