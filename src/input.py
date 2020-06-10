from cartesian_point import CartesianPoint
from sympy.core.function import Function
from sympy.core.symbol import Symbol
from sympy.parsing.sympy_parser import parse_expr


class EntradaDeDados:

    pontos: list
    calcularErro: bool
    pontoDeInteresse: CartesianPoint
    funcao: Function

    def __init__(self):
        self.pontos = []
        self.calcularErro = False
        self.funcao = ''
        self.pontoDeInteresse = None

    def pegarDados(self):
        self.coletarPontos()
        while True:
            r = input('\nDeseja calcular o erro? "s" ou "n" >>').lower()
            if r == 'n':
                break
            if r == 's':
                self.coletarDadosParaErro()
                break
        print('\nDados coletados: ')
        print('\tpontos:')
        for ponto in self.pontos:
            print(f'\t\t({ponto.x}; {ponto.y})')
        if self.calcularErro:
            print(f'\tpontoDeInteresse: ({self.pontoDeInteresse.x}; {self.pontoDeInteresse.y})')
            print(f'\tfuncao: {self.funcao}')

    def coletarPontos(self):
        while True:
            it = len(self.pontos) + 1
            print(f'\nInforme os valores para o ponto: {it}')
            x = self.catchNumber('x: ', '\t')
            y = self.catchNumber('y: ', '\t')
            print(f'valores digitados: ({x}; {y})')
            self.registrarPonto(CartesianPoint(x, y))
            if self.sair() is True:
                break

        print('\nPontos informados: ')
        for ponto in self.pontos:
            print(f'({ponto.x}; {ponto.y})')

    def registrarPonto(self, ponto):
        while True:
            msg = '\tPara registrar o valor digite "r", para descartar o valor digite "d": '
            r = input(f'{msg}>>')
            if r.lower() == 'r':
                self.pontos.append(ponto)
                print('\tregistrado')
                break
            if r.lower() == 'd':
                print('\tdescartado')
                break

    def coletarDadosParaErro(self):
        print('Coletar dados para calculo do erro')
        pyExp = '**'
        normExp = '^'
        while True:
            funcao = input('\tdigite a função para calculo do erro: >>').replace(normExp, pyExp)
            funcao = parse_expr(funcao, evaluate=False)
            func_print = str(funcao).replace(pyExp, normExp)
            r = input(
                f'\tdeseja salvar a função: "{func_print}"? "s" ou "n": >>').lower()
            if r == 'n':
                continue
            if r == 's':
                self.funcao = funcao
                print('\tfunção salva')
                break
        while True:
            print('\tInforme o ponto de interesse: ')
            x: float = self.catchNumber('x: >>', '\t\t')
            y = self.funcao.evalf(subs={Symbol('x'): x})
            r = input(
                f'\tdeseja salvar o ponto: ({x}; {y})? "s" ou "n": >>').lower()
            if r == 'n':
                continue
            if r == 's':
                self.pontoDeInteresse = CartesianPoint(x, y)
                self.calcularErro = True
                print('\tPonto salvo')
                break

    def sair(self):
        while True:
            sair = input('Digite "s" para sair ou "c" para continuar: >>')
            if sair.lower() == 'c':
                return False
            if sair.lower() == 's':
                return True

    def catchNumber(self, msg: str, identacao: str):
        if identacao != None:
            msg = identacao + msg
        while True:
            try:
                number = float(input(msg).replace(',', '.'))
                return number
            except ValueError:
                print(f'{identacao}valor inválido')


# end of class
