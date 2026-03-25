import random

numero_aleatorio = random.randint(1, 10)

decisao = True

while(decisao):

    numero_escolhido = int(input("Digite um número de 1 a 10: "))

    if numero_escolhido != numero_aleatorio:
        print("Você errou tente novamente!")
        

    else:
        print("Parabéns você acertou!")
        break
