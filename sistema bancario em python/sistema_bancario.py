menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(menu)

def banco():
    global saldo, extrato, numero_saques
    
    while True:
        opcao = input("Escolha uma opção: ")
        
        if opcao == 'd':
            valor = int(input('Digite o valor que deseja depositar: '))
            if valor <= limite:
                saldo += valor
                extrato += f'Depósito: {valor}\n'
            else:
                print('O saldo ultrapassou o limite!')
                    
        elif opcao == 's':
            valor = int(input('Digite o valor que deseja sacar: '))
            if valor <= saldo and numero_saques < LIMITE_SAQUES:
                saldo -= valor
                extrato += f'Saque: {valor}\n'
                numero_saques += 1
            else:
                print('O valor que deseja sacar é maior que o saldo disponível ou o número de saques já ultrapassou o limite.')
                
        elif opcao == 'e':
            print(extrato)
            
        elif opcao == 'q':
            print('Sair')
            break
            
        else:
            print('Opção inválida, por favor selecione novamente a operação desejada!')

banco()
