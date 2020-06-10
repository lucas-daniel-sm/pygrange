#################################################
####  PyGrange by Lucas Daniel Silva Mendes  ####
####        CopyRigths reserved 2020         ####
#################################################
import json
from cartesian_point import CartesianPoint
from lagrange_solver import LagrangeSolver
from lagrange_error import LagrangeError
from input import EntradaDeDados


def calcular_erro(inputs: EntradaDeDados, result: map):
    print('\n')
    lagrange_error = LagrangeError({
        'lagrange_polinomial': result['final_polynomial'],
        'function': inputs.funcao,
        'points': inputs.pontos,
        'point': inputs.pontoDeInteresse.x
    })
    lagrange_error.calculate()
    return lagrange_error.result



inputs = EntradaDeDados()
inputs.pegarDados()

lagrange_solver = LagrangeSolver(inputs.pontos)
result = lagrange_solver.solve()
result_json = lagrange_solver.resultToJson(result)

print(result_json)

if inputs.calcularErro:
    r = calcular_erro(inputs, result)
    jsonErro = json.dumps(r, indent=4)
    print(f'\n{jsonErro}')