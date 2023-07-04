import turtle

prompt = input("Do you want a smaller or larger square? (input: smaller/larger)")
if prompt == "smaller":
    x = 30
else:
    x = 60

for j in range(4):
    turtle.forward(x)
    turtle.right(90)

turtle.done()
