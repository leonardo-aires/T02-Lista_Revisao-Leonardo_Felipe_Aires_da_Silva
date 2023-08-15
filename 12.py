# 12) Faça um programa que leia uma senha, até que a senha esteja correta.


senha_correta = "correta"

while True:
    senha = input("Insira a senha: ")
    
    if senha == senha_correta:
        print("A senha está correta!")
        break
    else:
        print("Senha incorreta. Tente novamente.")