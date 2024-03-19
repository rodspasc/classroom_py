# sintaxe geral: [expressão for item in lista]
# expressão é a expresão que será avaliada para cada elemento da lista, 
# e item é a variável que representa cada elemento na lista.

# numeros = [1,4,7,9,10,12,21]
# # quadrados = list(map(lambda num: num**2, numeros))
# quadrados = [num**2 for num in numeros]
# print(quadrados)

# pares = [num for num in range(1001) if num % 2 == 0]
# print(pares)
# print(len(pares))

# frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
# vogais = ['A','a','e','i','o','u','á','é','í','ó','ú']
# lista_vogais = [v for v in frase if v in vogais]
# print(f'A frase possui {len(lista_vogais)} vogais')
# print(lista_vogais)

# distributiva entre valores de duas listas

distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)  