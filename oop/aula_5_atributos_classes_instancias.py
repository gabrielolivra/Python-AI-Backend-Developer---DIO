class Estudante:
    escola = 'DIO'
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
    
def listar_alunos(*objs):
    for obj in objs:
        print(obj)
    


aluno1 = Estudante('Gabriel b', 998888)
aluno2 = Estudante('Teste2', 99999)

Estudante.escola = 'Outro nome escola'
# print(aluno1, aluno2)
listar_alunos(aluno1, aluno2)

aluno1.nome = 'Oliveira'

listar_alunos(aluno1, aluno2)