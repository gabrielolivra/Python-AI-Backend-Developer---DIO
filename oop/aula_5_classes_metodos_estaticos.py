class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)


    @staticmethod
    def maior_idade(idade):
        return 'maior de idade' if idade >= 18 else 'Menor de idade'

p = Pessoa.criar_de_data_nascimento(1998, 3, 21, 'Gabriel')

print(p.nome, p.idade)

print(p.maior_idade(17))