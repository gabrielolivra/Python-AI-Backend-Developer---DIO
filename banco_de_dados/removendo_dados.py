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

def remover_cliente(id):
    conexao = sql.connect('clientes.db')
    consulta = conexao.cursor()
    consulta.execute('DELETE FROM clientes WHERE id = ?', (id))
    conexao.commit()
    conexao.close()
    print("Cliente removido com sucesso")

remover_cliente(id)

