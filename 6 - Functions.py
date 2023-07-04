import turtle


def draw_square(pos_x, pos_y):
    turtle.setpos(pos_x, pos_y)
    turtle.pendown()
    for j in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.penup()


draw_square(0, 0)
draw_square(40, 0)
draw_square(0, 40)
draw_square(40, 40)

turtle.done()
