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
parallelogram(-255, 267, 35, 25, 40, '#8ECC23')
triangle(-270, 197, 50, 0, '#FEDD14')
triangle(-318, 145, 40, 90, '#4FBAE8')
triangle(-275, 171, 25, 270, '#A250E2')
triangle(-266, 180, 25, 225, '#EF66E8')

#fish

triangle(-101, 195, 30, 90, '#A250E2')
triangle(-38, 225, 30, 0, '#EF66E8')
parallelogram(-38, 228, 40, 30, 40, '#8ECC23')
square(0, 224, 25, 45, '#FF7C00')
triangle(-61, 159, 60, 0, '#FEDD14')
triangle(-1, 230, 60, 180, '#F72A49')
triangle(3, 190, 45, 495, '#4FBAE8')


#smth

parallelogram(140, 246, 40, 35, 355, '#8ECC23')
triangle(205, 252, 45, 135, '#4FBAE8')
triangle(203, 187, 62, 180, '#F72A49')
triangle(257, 208, 50, 0, '#FEDD14')
square(255, 212, 25, 0, '#FF7C00')
triangle(264, 241, 25, 135, '#EF66E8')
triangle(241, 187, 22, 45, '#A250E2')

#man

square(225, 73, 25, 45, '#FF7C00')
triangle(223, 10, 60, 180, '#F72A49')
triangle(287, 70, 60, 0, '#FEDD14')
triangle(227, 7, 30, 180, '#4FBAE8')
parallelogram(201, -53, 35, 30, 40, '#8ECC23')
triangle(265, -50, 23, 0, '#A250E2')
triangle(187, -72, 25, 0, '#EF66E8')

turtle.speed(15)
turtle.mainloop()
