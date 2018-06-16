from turtle import *

speed(-1)
shape("turtle")

def draw_star(x, y, lengthofstar):
    penup()
    setpos(x, y)
    pendown()
    for i in range(5):
        forward(lengthofstar)
        right(144)

draw_star(100, 100, 100)





mainloop()