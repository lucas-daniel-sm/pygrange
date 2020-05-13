from sympy import expand, collect, Symbol
import json


class LagrangeSolver:
    points: list

    def __init__(self, points: list):
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
            l_x_simplified_times_y = f'(({l_x_simplified}) * {y_n})'
            polynomials.append(l_x)
            simplified_polynomials.append(l_x_simplified)
            simplified_polynomials_times_y.append(l_x_simplified_times_y)

            if final_polynomial is None:
                final_polynomial = l_x_simplified_times_y
            else:
                final_polynomial = f'{final_polynomial} + {l_x_simplified_times_y}'

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

    def resultToJson(self, result: dict):
        polynomials = list(map(self.refact_expression, result['polynomials']))
        simplified_polynomials = list(map(self.refact_expression, result['simplified_polynomials']))
        simplified_polynomials_times_y = list(map(self.refact_expression, result['simplified_polynomials_times_y']))
        final_polynomial = self.refact_expression(result['final_polynomial'])
        final_polynomial_simplified = self.refact_expression(result['final_polynomial_simplified'])

        return json.dumps({
            'polynomials': polynomials,
            'simplified_polynomials': simplified_polynomials,
            'simplified_polynomials_times_y': simplified_polynomials_times_y,
            'final_polynomial': final_polynomial,
            'final_polynomial_simplified': final_polynomial_simplified
        }, indent=4)


    def refact_expression(self, expression):
        expression_string = str(expression).replace('**', '^')
        return expression_string

