import random

# for i in range(5):
#     valor = random.randint(1,50)
#     print(f'O número gerado é: {valor}')

# valor = random.random()
# print(f'O número gerado é : {round(valor * 10, 2)}')

# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 4)}')

L = [2,4,6,9,10,13,14,16,18,20,21,27,33]
# valor = random.choice(L)
# print(f'O número escolhido: {valor}')

# valor = random.sample(L,3)
# print(f'O números escolhidos: {valor}')

print(f'Lista ordenada: {L}')
random.shuffle(L)
print(f'Lista embaralhada: {L}')
