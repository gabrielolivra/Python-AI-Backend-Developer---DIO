arquivo = open('escrevendo_arquivo.txt', 'w')

arquivo.write('Escrevendo dados no arquivo')

arquivo.write('\n')

arquivo.write('testando')

arquivo.writelines(['\n','escrevendo', 'um', 'novo', 'texto'])

arquivo.close()