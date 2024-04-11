try:
    file = open("arquivo-null", "r")
    file.close()
    print("Arquivo encontrado e lido")

except FileNotFoundError as exc:
    print( exc, 'Arquivo não existe') 