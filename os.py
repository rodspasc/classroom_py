# renomear arquivos em massa

import os

os.chdir('D:\\classroom\\classroom_py\\teste') # entra pasta (diretório) onde tem arquivos a serem tratados
print(f'Diretório atual: {os.getcwd()}') # informa o a pasta para verificar se esta correto 

padrao_nome = input('Qual o padrão de nomes de arquivos a usar (sem a extensão) ? ') # pede o nome padrão desejado pelo usuário

for contador, arq in enumerate(os.listdir()):   # contador recebe números sequenciais , arq recebe nome do arquivo dentro do diretório
    if os.path.isfile(arq): # verifica de o nome passado em arq é arquivo ou pasta (diretório)
        nome_arq, exten_arq = os.path.splitext(arq) # separa o nome do arquivo e a extensão do arquivo e passa separado para variáveis
        nome_arq = padrao_nome + ' ' + str(contador + 1) # nome_arq recebe a concatenação de nome padrão, espaço e número sequencial como string
        nome_novo = f'{nome_arq}{exten_arq}' # nome_novo recebe a concatenação do nome do arquivo com extensão do arquivo
        os.rename(arq, nome_novo) # renomeia o arquivo usando o nome novo

print('\nArquivos renomeados')