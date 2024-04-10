class Conta:
    
    def __init__(self, saldo = 0):
        self._saldo = saldo
        
    
    def sacar(self, valor):
        
        if self._saldo >= valor:
            self._saldo -= valor
            
            return 'Saque realizado com sucesso'
        else:
            
            return f'Não foi possivel realizar o saque! Saldo insuficiente! Saldo atual: {self._saldo}'

    def depositar(self, valor):
        self.saldo += valor
        return 'Deposito realizado com sucesso!'
    
    def verificar_saldo(self):
        return self._saldo
        
c1 = Conta(500)

print(c1.sacar(550))

print(c1.verificar_saldo())