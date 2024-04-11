import os
import shutil
from pathlib import Path

#Pegar caminho
ROOT_PATH = Path(__file__).parent

# #Criar diretorio 
os.mkdir(ROOT_PATH / "novo-diretorio")

# #Criar arquivo no diretorio atual
arquivo  = open(ROOT_PATH / "criando-arquivo.txt", "w")

# #Renomear um arquivo
os.rename("criando-arquivo.txt", "test.txt")

# #Removendo arquivo
os.remove("test.txt")

shutil.move(ROOT_PATH / "test.txt", ROOT_PATH / "novo-diretorio" / "test.txt" )
#Fechar arquivo
arquivo.close()
