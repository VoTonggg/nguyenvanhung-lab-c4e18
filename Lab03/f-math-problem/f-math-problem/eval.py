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
    return result



# print("Hello World")
# result = calc(10, 5, "+")
# print(result)