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
