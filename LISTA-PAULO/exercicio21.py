frase = str (input("Digite uma frase: "))

if len(frase) >= 4:

    print(frase[3:])

else:
    print("A frase é curta demais para mostrar a partir do quarto caractere.")