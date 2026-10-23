import turtle

def draw(t, length):
    angle = 50
    factor = .6

    if length > 5:
        t.forward(length)
        t.left(angle)
        draw(t, factor * length)
        t.right(2 * angle)
        draw(t, factor * length)
        t.left(angle)
        t.backward(length)

"""PUT YOUR FUNCTIONS HERE"""

t = turtle.Turtle()
t.color("white")
t.speed(0)

screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
t.clear()

"""PUT YOUR DRAW CALLS HERE"""

draw(t, 100)

turtle.exitonclick()