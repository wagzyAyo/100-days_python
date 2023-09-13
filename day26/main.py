import pandas


alpha = pandas.read_csv("./day26/nato_alphabet.csv")
print(alpha)


Enter_name = input("Enter Name: ").upper()
sliced = list(Enter_name)
print(sliced)

new_dict = {row.code for (
    index, row) in alpha.iterrows() if row.letter in sliced}

print(new_dict)
