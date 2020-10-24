# Case-study #1
# Developers:   Braer P. (),
#               Kokorina D. (),
#               Sidorov S. ()
import turtle


def square(x, y, side, angle, color):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side: side length of a square
    :param angle: the angle of rotation of the square
    :param color: the color of the square
    :return: None
    """
    turtle.up()
    turtle.setposition(x, y)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.left(90)
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(angle)
    turtle.end_fill()
    turtle.done()

import turtle as t

def triangle(x, y, leg, angle, color):
    '''

    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param leg: a leg Fof a triangle
    :param hyp: a hypotenuse of a triangle
    :param angle: the angle of rotation of a triangle
    :param color: the color of a triangle
    :return: None
    '''

leg = 200
x = -100
y = -100
hyp = ((leg ** 2 + leg ** 2) ** 0.5)
color = ('#FEDD14')

t.penup()
t.goto(x, y)
t.begin_fill()
t.pencolor(color)
t.pendown()
t.forward(leg)
t.left(90)
t.forward(leg)
t.left(135)
t.forward(hyp)
t.fillcolor(color)
t.end_fill()
t.hideturtle()
t.mainloop()

