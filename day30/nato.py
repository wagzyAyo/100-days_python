import pandas


alpha = pandas.read_csv("./day26/nato_alphabet.csv")


new_dict = {row.letter: row.code for (
    index, row) in alpha.iterrows()}


def generate_phonetic():
    Enter_word = input("Enter Word: ").upper()
    sliced = list(Enter_word)

    try:
        new_list = [new_dict[char] for char in sliced]
    except KeyError:
        print("sorry only letters in the alphabets please")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()
