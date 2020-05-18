from lagrange_solver import LagrangeSolver
from sympy import Symbol, diff, Function
from cartesian_point import CartesianPoint


class LagrangeError:

    points: list
    point: float
    order: int

    def __init__(self, config: map):
        self.lagrange_polinomial = config['lagrange_polinomial']
        #self.original_function = config['original_function ']
        self.function = config['function']
        self.points = config['points']
        self.point = config['point']
        self.order = len(self.points)

    def calculate(self):
        m = self.calculate_m()
        multiplication = self.multiplication()
        expression = (f'{multiplication} * ({m}/({self.order}!))')
        factorial_order_plus_one = 6 #self.order!
        result = multiplication * m / factorial_order_plus_one
        print(f'E_t({self.point}) = {expression} = {result}')

    def calculate_m(self):
        last_derivative = self.function
        derivatives = []
        last_value: float
        maxValue = None
        values = []
        x = Symbol('x')

        for i in range(self.order):
            last_derivative = diff(last_derivative, x)
            derivatives.append(last_derivative)
        
        for point in self.points:
            value = last_derivative.subs(x, point.x)
            values.append(value)
            if maxValue is None:
                maxValue = value
            else:
                if value > maxValue:
                    maxValue = value
    
        print(f'calaculo do M = {maxValue}')
        print(f'\t >> derivadas:')
        for derivative in derivatives:
            print(f'\t\t{LagrangeSolver.simplify_expression(derivative, x)}')
        print(f'\t >> valores para a {self.order + 1}ª derivada:')
        for value in values:
            print(f'\t\t{value}')
        return maxValue

    def multiplication(self):
        expression = None
        acumulator = None
        for local_point in self.points:
            if expression is None:
                expression = (f'({self.point} - {local_point.x})')
            else:
                expression = (f'{expression} * ({self.point} - {local_point.x})')
            if acumulator is None:
                acumulator = self.point - local_point.x
            else:
                acumulator = acumulator * (self.point - local_point.x)

        print('Produtório')
        print(f'\t >> expressao: {expression}')
        print(f'\t >> resultado: {acumulator}\n')
        
        return acumulator
