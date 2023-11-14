"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()


leo.penup()
leo.goto(-130, -60)
leo.pendown()

leo.speed(10)
leo.color("green", "yellow")
leo.fillcolor("pink")
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob.penup
bob.goto(-130, -60)
bob.pendown()
bob.speed(60)

side_length: int = 300

i: int = 0
side_length = side_length * .97
while (i < 100):
    leo.forward(200)
    leo.right(40)
    leo.left(122.5)
    i = i + 1

done()