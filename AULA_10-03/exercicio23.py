frase = str(input("Digite uma frase: "))

frase2 = str(input("Digite outra frase: "))

indice_meio = len(frase) // 2
frase_final = frase[:indice_meio] + frase2 + frase[indice_meio:]
print(frase_final)
