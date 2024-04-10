# Heranças de classes Simples e Multipla



# Herança simples

class Veiculo:
    
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
        
    def ligar(self):
        print('Ligando o motor!')



class Motocicleta(Veiculo):
    
    def __init__(self,cor, placa, num_rodas, gasolina):
        super().__init__(cor, placa, num_rodas)
        self.gasolina = gasolina
    
    def verificar_gasolina(self):
        print(f"{'Possui gasolina' if self.gasolina else 'Não possui gasolina'}")
    



class Carro (Veiculo):
    pass



class Caminhao (Veiculo):
    pass


m1 = Motocicleta('Vermelha' ,'KKK-123', 2, False )

m1.ligar()

m1.verificar_gasolina()

