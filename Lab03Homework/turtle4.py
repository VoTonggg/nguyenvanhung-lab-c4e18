from turtle import *

speed(-1)
shape("turtle")

def draw_square(lengthofsquare, drawingcolor):
    color(drawingcolor)
    for i in range(4):
        forward(lengthofsquare)
        left(90)


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()