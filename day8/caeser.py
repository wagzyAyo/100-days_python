alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decode:\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(ted_text, shift_amount, headed_direction):
    wanted_text = ""
    if headed_direction == "decode":
        shift_amount *= -1
    for letter in ted_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        wanted_text += new_letter
    print(f"The {headed_direction}d text is {wanted_text}")


caeser(ted_text=text, shift_amount=shift, headed_direction=direction)
