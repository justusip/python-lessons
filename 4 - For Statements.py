# We ask them to hardcode and draw a square first, then we ask if there is a way to make it more efficiently.

# Hardcoded version:
import turtle

t = turtle.Turtle()

t.forward(30)
t.right(90)

t.forward(30)
t.right(90)

t.forward(30)
t.right(90)

t.forward(30)
t.right(90)

# Optimized version:

import turtle

t = turtle.Turtle()

for j in range(4):
    t.forward(30)
    t.right(90)
