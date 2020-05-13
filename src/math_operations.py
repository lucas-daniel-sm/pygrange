from sympy import expand, collect, Symbol


class MathOperations:
    lagrange_result = {
        'functions_list': [],
        'simplified_functions': [],
        'functions_times_y_list': [],
        'final_function': None,
        'simplified_final_function': None
    }
    points: list

    def __init__(self, points: list) -> None:
        self.points = points

    def solve(self):
        var = Symbol('x')
        final_polynomial = None
        polynomials = []
        simplified_polynomials = []
        simplified_polynomials_times_y = []

        for i in range(len(self.points)):
            l_x = self.polynomial(i)
            l_x_simplified = self.simplify_expression(l_x, var)
            y_n = self.points[i].y

            polynomials.append(l_x)
            simplified_polynomials.append(self.simplify_expression(l_x, var))
            simplified_polynomials_times_y.append(l_x_simplified)

            if final_polynomial is None:
                final_polynomial = f'({l_x_simplified} * {y_n})'
            else:
                final_polynomial = f'{final_polynomial} + {l_x_simplified} * {y_n}'

        return {
            'polynomials': polynomials,
            'simplified_polynomials': simplified_polynomials,
            'simplified_polynomials_times_y': simplified_polynomials_times_y,
            'final_polynomial': final_polynomial,
            'final_polynomial_simplified': self.simplify_expression(final_polynomial, var)
        }

    def polynomial(self, n: int):
        expression_string = None
        local_points = self.points.copy()
        x_j = local_points.pop(n).x

        for ponto in local_points:
            x_i = ponto.x
            format_string = f'(x-{x_i})/({x_j}-{x_i})'
            if expression_string is None:
                expression_string = format_string
            else:
                expression_string = f'{expression_string} * {format_string}'

        return expression_string

    @staticmethod
    def simplify_expression(input_function, variable: Symbol):
        return expand(collect(input_function, variable))
