def eh_palindromo(frase):
    frase = frase.replace(" ", "")
    frase = frase.lower()
    return frase == frase[::-1]

frase = str(input("Digite uma frase: "))

print(eh_palindromo(frase))