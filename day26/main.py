with open("./day26/file1.txt") as file1:
    new_file_1 = [int(number.strip()) for number in file1.readlines()]
    print(new_file_1)


with open("./day26/file2.txt") as file2:
    new_file_2 = [int(number.strip()) for number in file2.readlines()]
    print(new_file_2)

result = [number for number in new_file_1 if number in new_file_2]
print(result)
