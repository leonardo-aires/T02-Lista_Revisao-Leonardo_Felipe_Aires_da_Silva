num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
op = input("Insira o operador: ")


if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Operador inválido")
    exit()


print("Resultado = ", result)