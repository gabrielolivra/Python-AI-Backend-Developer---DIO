import sqlite3 as sql

def consulta_sql(email):
    conexao = sql.connect("clientes.db")
    consulta = conexao.cursor()
    consulta.execute('SELECT email FROM clientes WHERE email = ?', (email,))
    resultado = consulta.fetchone()
    conexao.close()
    if resultado is not None:
        return False
    else:
        return True


nome = input('Digite o nome: ')
email = input('Digite o email: ')

if consulta_sql(email):

    conexao = sql.connect("clientes.db")

    consulta = conexao.cursor()

    consulta.execute('INSERT INTO clientes(nome, email) VALUES (?, ?) ', (nome, email))

    conexao.commit()

    conexao.close()

    print('Cadastro realizado com sucesso!')

else:
    print('Email já cadastrado no sistema!')
