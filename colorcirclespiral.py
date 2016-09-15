import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["cyan", "orange", "purple", "red", "green"]
for x in range(1000):
    t.pencolor(colors[x%5])
    t.circle(x)
    t.left(21)
