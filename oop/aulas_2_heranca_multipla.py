class Animal:
    
    def __init__(self, n_patas):
        self.n_patas = n_patas
        
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)
    pass


class Ave(Animal):
    
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)
    pass



class Cachorro(Mamifero):
    pass



class Ornitorrinco(Mamifero, Ave):
    pass


cachorro1 = Cachorro(n_patas = 4, cor_pelo= 'Branca')

print(cachorro1)

# QUANDO USAR O **kwargs passar o parametro por chave e valor. Exemplo abaixo

o = Ornitorrinco(n_patas = 2, cor_pelo='Preta', cor_bico = 'azul')

print(o)