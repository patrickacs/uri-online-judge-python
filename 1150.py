x = int(input())
y = 0
while y <= x:
    y = int(input())


def contagem():
    soma = 0
    a = 0
    for c in range(x, y):
        soma = soma + c
        a += 1
        if soma > y:
            print(a)
            return


contagem()