# 7) Encontrar a soma dos números inteiros a partir de 1 até N, com incrementos de 3 em 3. Exemplo: 1+4+7+10+13+16+19, para N=19.


num = int(input("Insira o número: "))


my_list = []


i = 1
while i <= num:
    my_list.append(i)
    i += 3


print(my_list)


result = sum(my_list)


print("Soma: ", result)