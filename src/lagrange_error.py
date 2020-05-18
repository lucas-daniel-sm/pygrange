from lagrange_solver import LagrangeSolver
from sympy import Symbol


class LagrangeError:

    points: list
    point: float
    order: int

    def __init__(self, original_function, lagrange_polinomial, points: list, point: float):
        self.original_function = original_function 
        self.lagrange_polinomial = lagrange_polinomial
        self.points = points
        self.point = point

    def calculate(self):
        multiplication = multiplication_point_points()
        m = calculate_m()
        expression = (f'{multiplication} * ({m}/({order}!)')
        print('Erro = {expression}')
        result = expression.subs(Symbol('x'), point)
        print(result)

    def calculate_m(self):
        for i in range(len(points)):
            print(f'derivada {1} = ')

    def multiplication_point_points(self):
        expression = ''
        for local_point in points:
            expression = (f'{expression} * ({point} - {local_point})')
        simplified_expression = LagrangeSolver.simplify_expression(expression)
        print(f'expressao: {expression}')
        print (f'simplificado: {simplified_expression}')

        return 
