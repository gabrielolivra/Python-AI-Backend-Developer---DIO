import csv

try:
    with open("nomes.csv", "r", newline="") as nomes:
        ler = csv.reader(nomes)
        for row in ler:
            print(row)
except IOError:
    print("Erro ao ler arquivo csv")