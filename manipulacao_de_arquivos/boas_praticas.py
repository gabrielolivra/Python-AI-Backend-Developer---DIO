
# Boas praticas para manipular arquivos com segurança
try:
    with open('arquivo.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as erro:
    print('Erro ao abrir o arquivo', erro)
    
#Não consegue ler arquivo fora do escopo   
print(arquivo.read())