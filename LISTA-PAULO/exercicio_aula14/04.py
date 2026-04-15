frase = str(input("Digite uma frase: "))

frase = frase.replace(" ", "").lower()

 
i = 0
soma = 0
while i < len(frase):
    
    if frase[i] in "aeiou":
        soma += 1
        
    i += 1
        
print(f"Essa frase tem {soma} vogais no total.")
    
    