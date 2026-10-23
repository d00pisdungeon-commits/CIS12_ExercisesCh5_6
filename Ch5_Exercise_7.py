import turtle


def draw_triangle(t, p1, p2, p3):
    """Helper function to draw a simple wireframe triangle between 3 points."""
    t.penup()
    t.goto(p1)
    t.pendown()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)  # Complete the triangle


def get_midpoint(p1, p2):
    """Helper function to find the absolute center between two coordinate points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski_coordinate(t, order, p1, p2, p3):
    """Recursively subdivides coordinates into clean wireframe layers."""
    if order == 0:
        # Base Case: Just trace the outer edge of these 3 coordinates
        draw_triangle(t, p1, p2, p3)
    else:
        # Get the midpoints of all three outer line segments
        mid_12 = get_midpoint(p1, p2)
        mid_23 = get_midpoint(p2, p3)
        mid_31 = get_midpoint(p3, p1)

        # Recursively draw the 3 sub-triangles in their precise zones
        sierpinski_coordinate(t, order - 1, p1, mid_12, mid_31)  # Bottom Left
        sierpinski_coordinate(t, order - 1, mid_12, p2, mid_23)  # Top Center
        sierpinski_coordinate(t, order - 1, mid_31, mid_23, p3)  # Bottom Right


# --- Screen & Window Configuration ---
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=700, height=700)
screen.title("Fixed Coordinate Sierpiński Triangle")

user_order = screen.numinput("Fractal Depth", "Enter recursion depth (0 to 6):", default=1, minval=0, maxval=6)
user_length = screen.numinput("Triangle Size", "Enter base side length (e.g., 400):", default=400, minval=100,
                              maxval=600)

if user_order is not None and user_length is not None:
    order = int(user_order)
    length = int(user_length)

    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    t.pensize(2)
    t.hideturtle()

    # Define the 3 absolute mathematical vertices of the main triangle
    # (Centered relative to 0,0)
    height = (3 ** 0.5 / 2) * length
    points = [
        (-length / 2, -height / 3),  # Bottom Left Point
        (0, 2 * height / 3),  # Top Peak Point
        (length / 2, -height / 3)  # Bottom Right Point
    ]

    # --- Draw execution ---
    sierpinski_coordinate(t, order, points[0], points[1], points[2])

screen.exitonclick()
