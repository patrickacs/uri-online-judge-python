tempo_bo = 0
tempo_arq = 0
tempo_mu = 0
tempo_des = 0

brinquedos = 0
n = int(input())

for i in range(n):
    elfo = input().split()
    nome = elfo[0]
    grupos = elfo[1]
    horas = int(elfo[2])
    if grupos=='bonecos':
        tempo_bo += horas
    if grupos=='arquitetos':
        tempo_arq += horas
    if grupos=='musicos':
        tempo_mu += horas
    if grupos=='desenhistas':
        tempo_des += horas

bonecos = (tempo_bo//8)+(tempo_arq//4)+(tempo_mu//6)+(tempo_des//12)
print(bonecos)