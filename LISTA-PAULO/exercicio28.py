emprestimo = float(input("Digite o valor do emprestimo que deseja fazer: "))
salario= float(input("Digite o valor de seu salario: "))
qtd_meses = int(input("Digite a quantidade de meses para se pagar o emprestimo: "))

prestacao_mensal = emprestimo // qtd_meses

if prestacao_mensal > salario * 30/100:
    print("A operação não pode ser feita, pois o valor de prestação mensal é maior que 30% do seu salario")

else:
    print("Deu certo o seu emprestimo!") 