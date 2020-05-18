#################################################
####  PyGrange by Lucas Daniel Silva Mendes  ####
####        CopyRigths reserved 2020         ####
#################################################
import json
from cartesian_point import CartesianPoint
from lagrange_solver import LagrangeSolver
from lagrange_error import LagrangeError

y_0 = 1.1414
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

def calcular_erro():
    print(result_json)
    print('\n')
    lagrange_error = LagrangeError({
        'lagrange_polinomial': result['final_polynomial'],
        'function': 'sqrt(1+x)',
        'points': points,
        'point': 0.45
    })
    lagrange_error.calculate()

# Caso não queira calcular o erro descomente a linha abaixo
calcular_erro()
