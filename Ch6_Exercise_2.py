import math

def hypot(a, b):
    c_squared = a**2 + b**2
    return math.sqrt(c_squared)

print(f"Test Step: {hypot(3, 4)}")