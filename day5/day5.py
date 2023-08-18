import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
           ]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '&', '^', '(', ')', '+']
print("Welcome to the password Generator !")
unit_letters = int(input("How many letters do you want in your password\n "))
unit_numbers = int(input("How many numbers do you want in your password\n "))
unit_symbols = int(input("How many symbols do you want in your password\n "))
password = ''
lett = ''
numb = ''
symb = ''
for x in range(1, unit_letters + 1):
    lett = random.choice(letters)
    password += lett

for x in range(1, unit_numbers + 1):
    numb = str(random.choice(numbers))
    password += numb

for x in range(1, unit_symbols + 1):
    symb = random.choice(symbols)
    password += symb

password = ''.join(random.sample(password, len(password)))
print(password)
