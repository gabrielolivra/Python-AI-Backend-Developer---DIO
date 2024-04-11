import csv

try:
    with open("nomes.csv", "w", encoding='utf-8') as arquivo:
       escrito =  csv.writer(arquivo)
       escrito.writerow(["id", "Nome"])
       escrito.writerow(["1", "Joao"])
       escrito.writerow(["2", "Maria"])
       escrito.writerow(["3", "Jose"])
except IOError as exc:
    print("Erro ao criar o arquivo")