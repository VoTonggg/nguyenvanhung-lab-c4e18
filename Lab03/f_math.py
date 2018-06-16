from random import choice
# from eval import calc
import eval
x = choice(range(1,10))
y = choice(range(1,10))
ops = ["+", "-", "*", "/"]
# result = 0
op = choice(ops)

# if op == "+":
#     result = x + y
# elif op == "-":
#     result = x - y
# elif op == "*":
#     result = x * y
# elif op == "/":
#     result = x / y

result = eval.calc(x, y, op)

errors = [-1, 0, 0, 1, 0, 0]
error = choice(errors)

print("* "*20)
print("{0} {1} {2} = {3}".format(x, op, y,result + error))
print("* "*20)

ans = input("Y/N? ").upper()
if error == 0:
    if ans == "N":
        print("You are wrong")
    elif ans == "Y":
        print("Yay")
else:
    if ans == "N":
        print("Yay")
    elif ans == "Y":
        print("You are wrong")

