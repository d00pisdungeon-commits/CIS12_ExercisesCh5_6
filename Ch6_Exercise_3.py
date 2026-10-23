def is_between(x, y, z):
    return x < y < z or z < y < x

print(is_between(5, 8, 3))