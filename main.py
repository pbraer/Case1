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


def triangle(x, y, leg, angle, color):
    """
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param leg: a leg Fof a triangle
    :param hyp: a hypotenuse of a triangle
    :param angle: the angle of rotation of a triangle
    :param color: the color of a triangle
    :return: None
    """

    hyp = ((leg ** 2 + leg ** 2) ** 0.5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.right(angle)
    turtle.pencolor(color)
    turtle.pendown()
    turtle.forward(leg)
    turtle.left(90)
    turtle.forward(leg)
    turtle.left(135)
    turtle.forward(hyp)
    turtle.left(45)
    turtle.right(angle)
    turtle.fillcolor(color)
    turtle.end_fill()



def parallelogram(x, y, side1, side2, angle, color):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side1: the longest side of a parallelogram
    :param side2: the shortest side of a parallelogram
    :param angle: the angle of rotation of the parallelogram
    :param color: the color of the parallelogram
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
    turtle.forward(side1)
    turtle.left(40)
    turtle.forward(side2)
    turtle.left(140)
    turtle.forward(side1)
    turtle.left(40)
    turtle.forward(side2)
    turtle.left(140)
    turtle.left(angle)
    turtle.end_fill()

#rabbit

triangle(-319, 200, 50, 0,'#F72A49')
square(-266, 264, 25, 0, '#FF7C00')
parallelogram(-255, 267, 36, 25, 40, '#8ECC23')
triangle(-270, 197, 50, 0, '#FEDD14')
triangle(-318, 145, 40, 90, '#4FBAE8')
triangle(-275, 175, 30, 270, '#A250E2')
triangle(-300, 210, 30, 90, '#EF66E8')

#fish


turtle.hideturtle()
turtle.mainloop()
