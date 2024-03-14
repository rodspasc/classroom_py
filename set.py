# set não permite elementos duplicados, suporta matematica de conjuntos, 
# não permite modificar itens mas permite adicionar novos itens

# planeta_anao = {'Plutão','Ceres','Eris','Haumea','Makemake'}
# print(planeta_anao)
# print(type(planeta_anao))
# print(len(planeta_anao))
# print('Ceres' in planeta_anao)
# print('Lua' in planeta_anao)
# print('Lua' not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper(), end = ' & ')

# for astro in planeta_anao:
#     print(astro.upper())    

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros, end = ' ')
# astros_set = set(astros)
# print(astros_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte','Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Halley'}
# print(astros1 != astros2)
# print(astros1 == astros2)
# print(astros1 | astros2)
# print(astros1.union(astros2))
# print(astros1 & astros2)
# print(astros1.intersection(astros2))
# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2))

astros1.add('Urano')
astros2.add("Sol")
print(astros1)
print(astros2)

astros1.remove('Lua')
astros1.discard('Terra') # não apresenta erro no caso do elemento não existir no conjunto
astros2.pop() # remove aleatoriamente um elemento do conjunto
print(astros1)
print(astros2)

astros1.clear()
astros2.clear()
print(astros1)
print(astros2)
