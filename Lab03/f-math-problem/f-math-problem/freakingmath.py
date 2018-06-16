from random import *
from eval import calc
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = choice(range(1,10))
    y = choice(range(1,10))
    op = choice(["+", "-", "*", "/"])
    
    result = calc(x, y, op)
    error = choice([-1, 0, 1])
    display_result = result + error
    
    return [x, y, op, display_result]


def check_answer(x, y, op, display_result, user_choice):
    result = calc(x, y, op)
    if display_result == result :
        return user_choice
    else:
        return not user_choice

    
