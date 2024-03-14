elemento = {
    'Z': 3,
    'nome': 'Litio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionário possui {len(elemento)} elementos')

# atualizar uma entrada

# elemento['grupo'] = 'Alcalinos'
# print(elemento)

# adicionar entrada

# elemento['periodo'] = 1
# print(elemento)

# exclusão de itens em dicionarios

# del elemento['periodo']
# print(elemento)

# apagar todo conteudo do dicionario

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

# retorna itens do dicionario em tuplas

print(elemento.items())

for i in elemento.items():
    print(i)

for i in elemento.keys():
    print(i)  

for i in elemento.values():
    print(i)      

# desempacotar chaves e valores

for i, j in elemento.items():
    print(f'{i}: {j}')
