#################################################
####  PyGrange by Lucas Daniel Silva Mendes  ####
####        CopyRigths reserved 2020         ####
#################################################
import json
from cartesian_point import CartesianPoint
from lagrange_solver import LagrangeSolver

y_1 = 1.2649
y_2 = 1.3784

points = [
    CartesianPoint(0, y_0),
    CartesianPoint(0.6, y_1),
    CartesianPoint(0.9, y_2)
]

lagrange_solver = LagrangeSolver(points)
result = lagrange_solver.solve()
result_json = lagrange_solver.resultToJson(result)
print(result_json)

