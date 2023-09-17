try:
    file = open("a.txt")
    dict = {"key": "value"}
    dict["key"]
except FileNotFoundError as message:
    print(f"{message} File does not exist")
    file = open("a.txt", mode="w")
    file.write("something")
except KeyError as message:
    print(f"The key {message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
