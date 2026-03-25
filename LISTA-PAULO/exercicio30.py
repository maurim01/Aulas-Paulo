frase = str(input("Digite uma frase qualquer: ")).lower()

letrasA = frase.count("a")
letrasE = frase.count("e")
letrasI = frase.count("i")
letrasO = frase.count("o")
letrasU = frase.count("u")

total = letrasA + letrasE + letrasI + letrasO + letrasU

print(f"total de vogais é: {total}")