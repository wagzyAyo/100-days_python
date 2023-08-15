import random
test_seed = int(input("Create seed number: "))
random.seed(test_seed)

# Split string method
nameSAsCSV = input("Give everybody's names, seperated space by commas.: ")
name = nameSAsCSV.split(", ")
length = len(name)
last_element = length - 1
random_number = random.randint(0, last_element)
random_name = name[random_number]
print("{} Will pay the bill!".format(random_name))
