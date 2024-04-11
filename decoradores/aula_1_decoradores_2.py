def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes')
        funcao(*args, **kwargs)
        print('Faz algo depois')
        
    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"meu nome é {nome}")


ola_mundo('Gabriel')