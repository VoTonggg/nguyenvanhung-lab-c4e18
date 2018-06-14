from random import choice 

# function arguments / parameters
def calc(x , y, op):
    result = 0
    # op = choice(["+", "-", "*", "/"])

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y

    print(result)

calc(10, 5, "+")