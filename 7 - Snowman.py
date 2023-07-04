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


# You cant change anything under this

# Draw Body
draw_circle(0, -40, 30, "black", "white")
draw_circle(0, -100, 40, "black", "white")
draw_circle(0, -200, 60, "black", "white")

# Draw Eyes
draw_circle(-10, -10, 2, "black", "white")
draw_circle(10, -10, 2, "black", "white")

# Draw Nose
draw_circle(0, -15, 3, "black", "orange")

# Draw Buttons
draw_circle(0, -35, 2, "black", "white")
draw_circle(0, -45, 2, "black", "white")
draw_circle(0, -55, 2, "black", "white")

# Draw Left Arm
draw_hand(-39, -50, 50, 160, "black", "white")

# Draw Right Arm
draw_hand(39, -50, 50, 20, "black", "white")

# Draw Hat
draw_square(-25, 15, 50, "black", "white")
draw_rectangle(-50, 15, 100, 10, "black", "white")

turtle.done()
