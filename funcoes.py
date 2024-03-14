# Modularização, reuso de código, legibilidade

# sem argumnetos
def mensagem():
    print('Curso UNIVESP')
    print('Não recomendado para aprender')

# mensagem() # chama a função que executa o que está definido na função

# # com argumnetos
def soma(a, b):
    print(a+b)

# soma(12, 7)    

# # para poder usar os daddos de saida da função em outro codigo usamos return

def soma2(a,b):
    return a+b

# print(soma2(15,5))

# calc = soma2(15,5) + 5
# print(calc)

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x**2)
    return quadrados 

if __name__ == '__main__':
    valores = [2,5,7,8,9]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)

    mensagem()    


