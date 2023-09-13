sentence = "What is the Airspeen velocity of an unladen swallow"

new_list = sentence.split()

result = {word: len(word) for word in new_list}

print(result)
