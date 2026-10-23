import turtle


def sierpinski_wireframe(t, order, length):
    """Recursively draws a wireframe Sierpiński triangle using pure relative movements."""
    if order == 0:
        # Base Case: Draw an outline of an equilateral triangle
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        # Recursive Case: Subdivide into three smaller wireframe triangles

        # 1. Draw the Bottom-Left triangle
        sierpinski_wireframe(t, order - 1, length / 2)

        # 2. Move to the right, draw the Bottom-Right triangle, and come back
        t.forward(length / 2)
        sierpinski_wireframe(t, order - 1, length / 2)
        t.backward(length / 2)

        # 3. Move up the left side, draw the Top triangle, and come back
        t.left(60)
        t.forward(length / 2)
        t.right(60)

        sierpinski_wireframe(t, order - 1, length / 2)

        t.left(60)
        t.backward(length / 2)
        t.right(60)


# --- Screen & Window Configuration ---
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=700, height=700)
screen.title("Working Relative Sierpiński Triangle")

# --- Graphical User Input Prompts ---
user_order = screen.numinput(
    "Fractal Depth",
    "Enter recursion depth (0 to 6):",
    default=1,
    minval=0,
    maxval=6
)

user_length = screen.numinput(
    "Triangle Size",
    "Enter base side length in pixels (e.g., 200 to 500):",
    default=400,
    minval=100,
    maxval=600
)

if user_order is not None and user_length is not None:
    order = int(user_order)
    length = int(user_length)

    # --- Turtle Configuration ---
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    t.pensize(2)
    t.hideturtle()

    # Position turtle near the bottom-left so the shape is centered
    t.penup()
    t.goto(-length / 2, -length / 3)
    t.pendown()

    # --- Draw execution ---
    sierpinski_wireframe(t, order, length)

# Keep window active in PyCharm until clicked
screen.exitonclick()
