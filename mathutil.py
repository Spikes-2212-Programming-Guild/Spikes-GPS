import math


def tocartesian(norm, arg):
    return norm * math.cos(arg), norm * math.sin(arg)


def rotate(x, y, angle):
    norm = math.sqrt(x * x + y * y)
    arg = math.atan2(y, x)
    return tocartesian(norm, arg + angle)


def cosinelaw(side1, side2, angle):
    return math.sqrt(side1 * side1 + side2 * side2 - 2 * side1 * side2 * math.cos(angle))
