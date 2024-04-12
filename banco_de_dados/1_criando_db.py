import sqlite3 as sql

# criando banco de dados
conexao = sql.connect("clientes.db")

print(conexao)

cur = conexao.cursor()

cur.execute("CREATE TABLE  clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

cur.close()

