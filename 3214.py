n = int(input())
for i in range(n):
    soma = 0
    lista = input().split(" ")
    for j in range(len(lista)):
        lista[j] = int(lista[j])
        if j != 0 and j != len(lista) - 1:
            soma += lista[j] - 1
        elif j == len(lista) - 1:
            soma += lista[j]
    print(soma)