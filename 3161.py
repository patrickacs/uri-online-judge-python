entrada = input().split()
quantidade_frutas = int(entrada[0])
linhas_lista = int(entrada[1])

vetor_frutas = [""] * quantidade_frutas

vetor_linhas = [""] * linhas_lista

for i in range(quantidade_frutas):
    vetor_frutas[i] = input().lower()

for i in range(linhas_lista):
    vetor_linhas[i] = input().lower()

for i in vetor_frutas:
    Come = False
    fruta_inversa = i[::-1]

    for j in vetor_linhas:
        if (i in j) or (fruta_inversa in j):
            Come = True
            break

    if Come:
        print("Sheldon come a fruta", i)
    else:
        print("Sheldon detesta a fruta", i)