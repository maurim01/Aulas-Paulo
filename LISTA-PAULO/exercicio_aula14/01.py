i = 0
soma = 0

qtd = int(input("Quantos números você deseja fazer a soma: "))

while i < qtd:
    num = int(input(f"Digite o valor do num{i+1}: "))
    
    soma += num
    i += 1
    
media = soma/(qtd)

print(f"Sua média é:{media}")