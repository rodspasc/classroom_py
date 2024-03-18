# recursividade
# fórmula geral para fatorial:
# fatorial(num) = 1, se num = 0 ou num =1 "caso base"
# fatorial(num) = num * fatorial(num -1), num > 1 "caso recursivo"

# 4! -> fatorial(4) = 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) = 
# = 4 * 3 * 2 * 1 = 24 

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num -1)
    
if __name__ == '__main__':
    x = int(input('Digite um número inteiro positivo para calcular o seu fatorial: '))
    try:
        res = fatorial(x)
    except RecursionError:       
        print('O número fornecido é muito grande ou negativo')       
    else:        
        print(f'O fatorial de {x} é {res}')    
    



