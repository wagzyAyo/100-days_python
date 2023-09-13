import pandas


alpha = pandas.read_csv("./day26/nato_alphabet.csv")


new_dict = {row.letter: row.code for (
    index, row) in alpha.iterrows()}

Enter_name = input("Enter Name: ").upper()
sliced = list(Enter_name)
new_list = [new_dict[char] for char in sliced]

print(new_list)
