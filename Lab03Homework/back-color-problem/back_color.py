from random import *
from check_point import is_inside
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = choice(['RED', 'GREEN', 'BLUE', 'YELLOW'])
    color_text = choice(['#3F51B5', '#FFD600', '#4CAF50', '#C62828']) 
    quiz_type = randint(0, 1)
    return [
                text,
                color_text,
                quiz_type
            ]

def mouse_press(x, y, text, color, quiz_type):
    for shape in shapes:
        if is_inside([x, y] , shape['rect']):
            print(shape['color'], shape['text'])
            if quiz_type == 0:
                if shape['text'].upper() == text:
                    return True
                else:
                    return False
            elif quiz_type == 1:
                if shape['color'] == color:
                    return True
                else:
                    return False      
            
            break

    

