from cartesian_point import CartesianPoint
from math_operations import *

points = [
    CartesianPoint(0, 1),
    CartesianPoint(0.5, 4.482),
    CartesianPoint(0.75, 9.488),
    CartesianPoint(1, 20.086)
]

result = MathOperations(points).solve()

print(result)
