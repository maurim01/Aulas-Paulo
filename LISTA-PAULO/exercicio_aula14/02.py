soma = 0
decisao = True
i = 0

while decisao:
    
    valor = float(input(f"Digite o valor do produto {i+1}: "))
    if valor == 0:
        
        decisao = False
        
    else:
        soma += valor
        i += 1
        
print(f"O valor total das compras é{soma}")
     