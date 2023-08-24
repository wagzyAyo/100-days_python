from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(ted_text, shift_amount, headed_direction):
    wanted_text = ""
    if headed_direction == "decode":
        shift_amount *= -1
    for char in ted_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            wanted_text += new_letter
        else:
            wanted_text += char
    print(f"The {headed_direction}d text is {wanted_text}")


print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decode:\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caeser(ted_text=text, shift_amount=shift, headed_direction=direction)
    result = input(
        "Do you want to continue? 'yes' if you want otherwise type 'no':\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
