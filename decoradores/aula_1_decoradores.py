def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de exc')
        funcao()
        print('faz algo deposi de exc')
        
    return envelope

def ola_mundo():
    print('Ola mundo')
    
    
ola_mundo = meu_decorador(ola_mundo)

ola_mundo()