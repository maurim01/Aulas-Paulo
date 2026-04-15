senha01 = "123456"
tentativas = 3
repetir = True

while repetir:
    
    senha_user = str(input("Digite sua senha: "))
    
    if senha_user != senha01:
        tentativas -= 1
        print(f"Senha incorreta você tem {tentativas} tentativas!")
        
        if tentativas == 0:
            print("Números de tentativas zeradas!")
            break
        
    elif senha_user == senha01:
        print("Senha correta!")
        break

    