import turtle

t = turtle.Turtle()


def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def create_line(x, y, length, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.setheading(angle + 20)
    t.forward(20)
    t.penup()
    t.back(20)
    t.pendown()
    t.setheading(angle - 20)
    t.forward(20)


def draw_rectangle(x, y, length, width):
    turtle.penup()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(length)
        else:
            turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()


def draw_square(x, y, length):
    turtle.penup()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()


# Draw Body
draw_circle("#ffffff", 30, 0, -40)
draw_circle("#ffffff", 40, 0, -100)
draw_circle("#ffffff", 60, 0, -200)

# Draw Eyes
draw_circle("#ffffff", 2, -10, -10)
draw_circle("#ffffff", 2, 10, -10)

# Draw Nose
draw_circle("#FF6600", 3, 0, -15)

# Draw Buttons
draw_circle("#ffffff", 2, 0, -35)
draw_circle("#ffffff", 2, 0, -45)
draw_circle("#ffffff", 2, 0, -55)

# Draw Left Arm
create_line(-39, -50, 50, 160)

# Draw Right Arm
create_line(39, -50, 50, 20)

# Draw Hat
draw_square(-25, 15, 50)
draw_rectangle(-50, 15, 100, 10)
