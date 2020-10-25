# Case-study #1
# Developers:   Braer P. (60%),
#               Kokorina D. (),
#               Sidorov S. (0%)
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
    turtle.left(45)
    turtle.forward(side2)
    turtle.left(135)
    turtle.forward(side1)
    turtle.left(45)
    turtle.forward(side2)
    turtle.left(135)
    turtle.left(angle)
    turtle.end_fill()

#rabbit

triangle(-319, 200, 50, 0,'#F72A49')
square(-266, 264, 25, 0, '#FF7C00')
parallelogram(-255, 267, 35, 25, 45, '#8ECC23')
triangle(-270, 197, 50, 0, '#FEDD14')
triangle(-318, 145, 40, 90, '#4FBAE8')
triangle(-275, 171, 25, 270, '#A250E2')
triangle(-266, 180, 25, 225, '#EF66E8')

#fish

triangle(-101, 195, 30, 90, '#A250E2')
triangle(-38, 225, 30, 0, '#EF66E8')
parallelogram(-38, 228, 40, 30, 45, '#8ECC23')
square(0, 224, 25, 45, '#FF7C00')
triangle(-61, 159, 60, 0, '#FEDD14')
triangle(-1, 230, 60, 180, '#F72A49')
triangle(3, 190, 45, 495, '#4FBAE8')


#smth

parallelogram(140, 246, 40, 35, 0, '#8ECC23')
triangle(205, 252, 45, 135, '#4FBAE8')
triangle(203, 187, 62, 180, '#F72A49')
triangle(257, 208, 50, 0, '#FEDD14')
square(255, 212, 25, 0, '#FF7C00')
triangle(264, 241, 25, 135, '#EF66E8')
triangle(241, 187, 22, 45, '#A250E2')

#right man

square(225, 73, 25, 45, '#FF7C00')
triangle(223, 10, 60, 180, '#F72A49')
triangle(287, 70, 60, 0, '#FEDD14')
triangle(227, 7, 30, 180, '#4FBAE8')
parallelogram(198, -50, 35, 30, 45, '#8ECC23')
triangle(265, -50, 23, 0, '#A250E2')
triangle(187, -65, 25, 0, '#EF66E8')

#big square
triangle(-150, -90, 150, 225, '#fede0c')
triangle(-148, 127, 150, 135, '#f72647')
triangle(65, 125, 75, 225, '#a34fe3')
square(10, 68, 72, 45, '#ff7d00')
triangle(5, -33, 67, 315, '#ef66e9')
triangle(-45, -95, 110, 90, '#4ebbe9')
parallelogram(8, -38, 100, 80, 90, '#8fcd1e')

#left man
square(-290, 110, 25, 45, '#ff7d00')
triangle(-240, 70, 60, 270, '#f72647')
parallelogram(-303, 70, 42, 33, 45, '#8fcd1e')
triangle(-335, -28, 60, 270, '#fede0c')
triangle(-325, -15, 20, 180, '#ef66e9')
triangle(-272, -60, 40, 225, '#4ebbe9')
triangle(-275, -52, 20, 225, '#a34fe3')

#yacht
triangle(-285, -100, 20, 0, '#a34fe3')
triangle(-285, -223, 70, 135, '#f72647')
triangle(-350, -218, 60, 180, '#fede0c')
square(-235, -222, 32, 45, '#ff7d00')
triangle(-238, -223, 30, 135, '#ef66e9')
triangle(-297, -226, 42, 315, '#4ebbe9')
parallelogram(-342, -226, 42, 41, 45, '#8fcd1e')

#helicopter
square(-150, -200, 32, 45, '#ff7d00')
triangle(-110, -210, 25, 225, '#ef66e9')
triangle(-55, -229, 25, 225, '#a34fe3')
triangle(-30, -165, 60, 315, '#fede0c')
triangle(-27, -250, 60, 135, '#f72647')
triangle(-33, -165, 42, 45, '#4ebbe9')
parallelogram(-22, -163, 50, 30, 90, '#8fcd1e')

#rocket
triangle(250, -115, 25, 315, '#ef66e9')
triangle(250, -152, 33, 0, '#4ebbe9')
triangle(215, -193, 50, 315, '#fede0c')
triangle(250, -162, 50, 135, '#f72647')
parallelogram(274, -255, 40, 30, 0, '#8fcd1e')
square(213, -235, 25, 45, '#ff7d00')
triangle(193, -255, 25, 225, '#a34fe3')

turtle.done()
