def tem_maiuscula(texto):#Função para verificar se há um caracter maiúsculo
    return any(char.isupper() for char in texto)

def tem_minuscula(texto):#Função para verificar se há um caracter minúsculo
    return any(char.islower() for char in texto)

def tem_numero(texto):#Função para verificar se há um número
    return any(char.isdigit() for char in texto)

i = True
while(i):
    
    senha = str(input("Digite sua senha: "))

    if len(senha) < 7:#Verificar o tamanho da senha
        print("A senha não tem 8 caracteres.")
        continue

    if tem_maiuscula(senha) == False:
        print("Sua Senha não contém um caracter maiusculo!")
        continue

    if tem_minuscula(senha) == False:
        print("Sua Senha não contém um caracter minusculo!")
        continue

    if tem_numero(senha) == False:
        print("Sua Senha não contém um número!")
        continue
    
    print("Senha valida!")
    break