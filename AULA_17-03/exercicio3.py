qtd_item = int(input("Digite a quantidade que você deseja adicionar: "))

item = 0

for i in range(qtd_item):
    item += float(input(f"Digite o valor do item {i+1}: "))

    valor_final= item - (item * 10/100)
    
print(f"O total do valor dos itens é  {int(valor_final)}")






