import turtle


def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        # Calculate the length of each of the 4 smaller segments
        segment_length = length / 3

        # Segment 1: Go straight
        koch(t, segment_length, depth - 1)

        # Segment 2: Turn left 60 degrees, go up-right
        t.left(60)
        koch(t, segment_length, depth - 1)

        # Segment 3: Turn right 120 degrees, go down-right
        t.right(120)
        koch(t, segment_length, depth - 1)

        # Segment 4: Turn left 60 degrees, go straight out
        t.left(60)
        koch(t, segment_length, depth - 1)


"""SCREEN SETUP"""
t = turtle.Turtle()
t.color("white")
t.speed(0)

screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=700, height=600)
t.clear()

"""POSITION THE TURTLE"""
# Move turtle to the left side of the screen so the curve fits nicely
t.penup()
t.goto(-300, -100)
t.pendown()

"""DRAW CALL"""
# Arguments: (turtle object, total pixel length, recursion depth/iterations)
koch(t, 600, 4)

turtle.exitonclick()