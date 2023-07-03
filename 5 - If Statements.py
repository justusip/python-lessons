import turtle

t = turtle.Turtle()

prompt = input("Do you want a smaller or larger square? (input: smaller/larger)")
if prompt == "smaller":
    x = 30
else:
    x = 60


for j in range(4):
    t.forward(x)
    t.right(90)
