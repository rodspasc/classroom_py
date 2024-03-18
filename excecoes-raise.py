# raise força um erro

from math import sqrt

class NumeroNegativoError(Exception):  # cria uma classe de erro 
    def __init__(self):
        pass


if __name__ == '__main__':
    while True: # laço infinito com tratamento de erro para o usuário digitar valor correto
        try:
            num = int(input('Digite um número positivo: '))
            if num < 0:
                raise NumeroNegativoError
            break
        except NumeroNegativoError:
            print('Não é permitido número negativo. Digite novamente.')
        
    print(f'A raiz quadrada de {num} é {sqrt(num)}')
    print('\nFim do cálculo')