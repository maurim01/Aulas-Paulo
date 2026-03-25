
decisao = True

while(decisao):

    num1 = int(input("Digite o valor do primeiro número: "))
    num2 = int(input("Digite o valor do segundo número: "))
    

    print("Qual operação você deseja fazer?\n" \
    "digite 1 para soma\n" \
    "digite 2 para subtração\n" \
    "digite 3 para multiplicação\n" \
    "digite 4 para divisão\n" \
    "digite 0 para sair")

    pergunta = int(input("Decisao: "))


    if pergunta == 1:
        soma = num1 + num2
        print(f"o resultado da soma é {soma}")
        
    

    if pergunta == 2:
        subtracao = num1 - num2
        print(f"o resultado da subtração é {subtracao}")
        

    if pergunta == 3:
        multiplicacao = num1 * num2
        print(f"o resultado da multiplicação é {multiplicacao}")
        

    if pergunta == 4:
        divisao = num1 / num2
        print(f"o resultado da divisao é {divisao}")
        
    if pergunta == 0:
        print("Obrigado por me usar!")
        break
