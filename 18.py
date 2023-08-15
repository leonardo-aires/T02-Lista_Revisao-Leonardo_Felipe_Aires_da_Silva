# 18)  Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato: "O número [número] é [par/ímpar]


num = int(input("Insira um número: "))


if num % 2 == 0:
    result = "par"
else:
    result = "ímpar"



print("O número", num, "é", result)