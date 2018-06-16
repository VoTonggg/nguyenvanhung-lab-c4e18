from turtle import *

speed(-1)
shape("turtle")

def draw_square(lengthofsquare, drawingcolor):
    color(drawingcolor)
    for i in range(4):
        forward(lengthofsquare)
        left(90)


draw_square(100, "red")

mainloop()