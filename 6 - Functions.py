import turtle

t = turtle.Turtle()


def draw_square(pos_x, pos_y):
    t.setpos(pos_x, pos_y)
    t.pendown()
    for j in range(4):
        t.forward(30)
        t.right(90)
    t.penup()


draw_square(0, 0)
draw_square(40, 0)
draw_square(0, 40)
draw_square(40, 40)
