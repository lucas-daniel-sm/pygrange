from lagrange_solver import LagrangeSolver
from sympy import Symbol, diff, Function
from cartesian_point import CartesianPoint
from numpy import math


class LagrangeError:
    points: list
    point: float
    order: int
    result: dict

    def __init__(self, config: dict):
        self.lagrange_polinomial = config['lagrange_polinomial']
        self.function = config['function']
        self.points = config['points']
        self.point = config['point']
        self.order = len(self.points)
        self.result = {}

    def calculate(self):
        m = self.calculate_m()
        multiplication = self.multiplication()
        expression = (f'{multiplication} * ({m}/({self.order}!))')
        factorial_of_order_plus_one = math.factorial(self.order)
        result = multiplication * m / factorial_of_order_plus_one
        self.result['erro'] = {
            'expression': expression, 
            'result': result
        }

    def calculate_m(self):
        last_derivative = self.function
        derivatives = []
        last_value: float
        maxValue = None
        values_for_last_derivative = []
        x = Symbol('x')

        for i in range(self.order):
            last_derivative = diff(last_derivative, x)
            derivatives.append(last_derivative)

        for point in self.points:
            value = float(last_derivative.subs(x, point.x))
            values_for_last_derivative.append(value)
            if maxValue is None:
                maxValue = value
            else:
                if value > maxValue:
                    maxValue = value
        
        self.result["m"] = {
            "derivatives": LagrangeSolver.refact_expression_list(derivatives),
            "last_derivative": LagrangeSolver.refact_expression(last_derivative),
            "values_for_last_derivative": values_for_last_derivative,
            "result": maxValue
        }
        
        return maxValue

    def multiplication(self):
        expression = None
        acumulator = None
        
        for local_point in self.points:
            if expression is None:
                expression = (f'({self.point} - {local_point.x})')
                acumulator = self.point - local_point.x
            else:
                expression = (f'{expression} * ({self.point} - {local_point.x})')
                acumulator = acumulator * (self.point - local_point.x)
        
        self.result['multiplication'] = {
            'expression': expression,
            'result': acumulator
        }
        
        return acumulator
