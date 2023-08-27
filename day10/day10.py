import art
print(art.logo)


def add(n1, n2):
    '''Sum two numbers'''
    return n1 + n2


def subtract(n1, n2):
    '''subtarct two numbers'''
    return n1 - n2


def divide(n1, n2):
    '''Divide two numbers'''
    return n1 / n2


def multiply(n1, n2):
    '''Multiply two numbers'''
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}
num1 = int(input("What is your first number: "))
for op in operations:
    print(op)
symbol_op = input("pick an operation from the line above: ")
num2 = int(input("What is your second number: "))


def ret():
    return


calc_op = operations[symbol_op]
answer_1 = calc_op(num1, num2)
print(f"{num1} {symbol_op} {num2} = {answer_1}")
continuety = True

while continuety:
    cont = input("do you want to continue 'y' to continue 'n' for NO: ")
    if cont == "n":
        continuety = False
        ret()
    symbol_op = input("pick an operation : ")
    calc_op2 = operations[symbol_op] 
    num3 = int(input("Enter another number: "))
    answer_2 = calc_op2(answer_1, num3)
    print(f"{answer_1} {symbol_op} {num3} = {answer_2}")
    answer_1 = answer_2
