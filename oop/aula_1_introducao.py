class Bicicleta:
    
#Metodo construtor __init___
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
        
    def buzinar(self):
        print('A bicicleta está buzinando')
    
    def parar(self):
        print('A bicicleta está parando')
    
    def correr(self):
        print('A bicicleta está parando')
        
#Listar dados do objeto de forma dinamica metodo __str__
   
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
# metodo destrutor  __del__

    def __del__(self):
        print('Removendo a instancia da classe')
        
        
        
bicicleta1 = Bicicleta('Vermelha', 'Monark', 1990, 1500)


bicicleta1.buzinar()

print(bicicleta1.__str__())