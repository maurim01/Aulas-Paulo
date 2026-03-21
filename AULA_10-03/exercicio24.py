frase = str(input("Digite uma frase: "))

if len(frase)%2 == 0:
    indice_meio = len(frase) // 2
    print(frase[:indice_meio] + " " + frase[indice_meio:])

else:
    print("A string tem numero impar de indices, não é possível dividir a string ao meio.")