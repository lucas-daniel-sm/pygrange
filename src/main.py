from sympy import *
from ponto_carteziano import PontoCarteziano


def main(): #{
    pontos = [
        PontoCarteziano(0, 1),
        PontoCarteziano(0.5, 4.482),
        PontoCarteziano(0.75, 9.488),
        PontoCarteziano(1, 20.086)
    ]
    function = solve(pontos)
    result = simplify_funtion(function, Symbol('x'))
    print('\n')
    print('\n')
    print(result)
    myResult = ''
#}


def solve(pontos: list): #{
    exp = None
    for i in range(len(pontos)):
        l_x = coeficiente(i, pontos)
        y_n = pontos[i].y
        print(f'l_x * y_x = {l_x} xxx {y_n}')
        print()
        print(simplify_funtion(l_x, Symbol('x')))
        print()
        if exp is None:
            exp = f'({l_x} * {y_n})'
        else:
            exp = f'{exp} + {l_x} * {y_n}'
    return exp
#}


def coeficiente(n: int, pontos: list): #{
    pontos_local = pontos.copy()
    x_j = pontos_local.pop(n).x
    expression_string = None

    for ponto in pontos_local:
        x_i = ponto.x
        format_string = f'(x-{x_i})/({x_j}-{x_i})'
        if expression_string is None:
            expression_string = format_string
        else:
            expression_string = f'{expression_string} * {format_string}'
    
    return expression_string
#}


def simplify_funtion(function, variable): #{
    return expand(collect(function, variable))
#}


main()
