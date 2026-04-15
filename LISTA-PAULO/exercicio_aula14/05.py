#O exercício propõe a criação de um simulador interativo de caixa eletrônico baseado em um laço de repetição while, 
# no qual o usuário parte de um saldo inicial predefinido e navega por um menu contínuo para realizar operações de consulta de saldo, 
# depósito ou saque, mantendo a execução do programa em loop até que a opção de encerramento seja explicitamente selecionada.

saldo = 1000.0

print("Bem vindo ao banco xerecard!\nDigite 1 para consultar seu saldo atual\nDigite 2 para sacar \nDigite 3 para realizar deposito \nDigite 0 para sair do nosso programa")

while True:
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        print(f"Seu saldo atual é {saldo}")
    
    elif opcao == 2:
        if saldo == 0:
            print("Ação inválida: Seu saldo é igual a 0")
            continue
        saque = float(input("digite a quantidade que sejesa sacar: "))
        if saque > saldo:
            print("Ação inválida: Saque não pode ser maior do que o saldo")
            continue
        else:
            saldo -= saque
            print(f"Seu saldo atual é {saldo}")
            continue
    elif opcao == 3:
        deposito = float(input("Digite o valor que sera depositado: "))
        saldo += deposito
        print(f"Seu saldo atual é {saldo}")
        
    elif opcao == 0:
        print("Saindo do sistema...")
        break        