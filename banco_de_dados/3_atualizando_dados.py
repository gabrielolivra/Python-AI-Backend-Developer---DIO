import sqlite3 as sql

conexao = sql.connect("clientes.db")


def consulta_usuarios():
    consulta = conexao.cursor()
    consulta.execute('SELECT * FROM clientes')
    clientes = consulta.fetchall()
    conexao.commit()
    conexao.close()
    return clientes



for cliente in consulta_usuarios():
    print( f"Id: {cliente[0]}, nome: {cliente[1]}, email: {cliente[2]}")


id = input('Digite o id que deseja atualizar: ')

print('Digite abaixo os campos que deseja atualizar')

nome = input('Nome: ')

email = input('Email: ')


def atualizar_cliente(id, nome, email):
    conexao = sql.connect("clientes.db")
    consulta = conexao.cursor()
    consulta.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
    conexao.commit()
    conexao.close()
    
atualizar_cliente(id, nome, email)