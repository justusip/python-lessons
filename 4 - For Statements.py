# We ask them to hardcode and draw a square first, then we ask if there is a way to make it more efficiently.

# Hardcoded version:
import turtle

turtle.forward(30)
turtle.right(90)

turtle.forward(30)
turtle.right(90)

turtle.forward(30)
turtle.right(90)

turtle.forward(30)
turtle.right(90)

turtle.done()

# Optimized version:

import turtle

for j in range(4):
    turtle.forward(30)
    turtle.right(90)

turtle.done()
