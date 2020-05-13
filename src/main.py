import json
from cartesian_point import CartesianPoint
from lagrange_solver import LagrangeSolver

points = [
    CartesianPoint(0, 1),
    CartesianPoint(0.5, 4.482),
    CartesianPoint(0.75, 9.488),
    CartesianPoint(1, 20.086)
]

lagrange_solver = LagrangeSolver(points)
result = lagrange_solver.solve()
result_json = lagrange_solver.resultToJson(result)
print(result_json)
