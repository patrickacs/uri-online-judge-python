n = int(input())
carrinhos = 0
bonecas = 0

for x in range(n):
    a, b = input().split(" ")
    if(b == "M"):
        carrinhos += 1
    else:
        bonecas += 1
print(f"{carrinhos} carrinhos\n{bonecas} bonecas")