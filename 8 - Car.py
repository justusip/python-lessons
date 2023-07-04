import turtle


def start_draw(x, y, line_colour, fill_colour):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(line_colour)
    if fill_colour is not None:
        turtle.fillcolor(fill_colour)
        turtle.begin_fill()
    turtle.pendown()


def end_draw():
    turtle.end_fill()
    turtle.penup()


def draw_hand(x, y, length, angle, line_colour, fill_colour):
    start_draw(x, y, line_colour, fill_colour)
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.setheading(angle + 20)
    turtle.forward(20)
    turtle.penup()
    turtle.back(20)
    turtle.pendown()
    turtle.setheading(angle - 20)
    turtle.forward(20)
    end_draw()


def draw_square(x, y, length, line_colour, fill_colour):
    start_draw(x, y, line_colour, fill_colour)
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    end_draw()


def draw_rectangle(x, y, length, width, line_colour, fill_colour):
    start_draw(x, y, line_colour, fill_colour)
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(length)
        else:
            turtle.forward(width)
        turtle.left(90)
    end_draw()


def draw_circle(x, y, radius, line_colour, fill_colour):
    start_draw(x, y, line_colour, fill_colour)
    turtle.circle(radius)
    end_draw()


def draw_windows(x, y):
    start_draw(x + 100, y + 50, "black", "gray")
    turtle.setheading(45)
    turtle.forward(70)
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(-45)
    turtle.forward(70)
    turtle.setheading(90)
    end_draw()

    start_draw(x + 200, y + 50, "black", None)
    turtle.forward(49.50)
    end_draw()


draw_rectangle(-200, 0, 400, 50, "black", "red")
draw_windows(-200, -0)
draw_circle(-100, 0, 20, "black", "black")
draw_circle(100, 0, 20, "black", "black")
