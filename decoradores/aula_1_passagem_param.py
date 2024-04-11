# função com parametros

def mensagem(nome):
    return f"Oi {nome}"


def mensagem_long(nome):
    return f"Olá tudo bem com voce {nome}"


def executar(funcao, nome):
    return funcao(nome)

print(executar(mensagem_long, 'Gabriel'))