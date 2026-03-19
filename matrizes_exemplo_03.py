linha = int(input("Digite a quantidade de linhas 
                  da matriz \t"))
coluna = int(input("Digite a quantidade de 
                   colunas da matriz \t"))
matriz = [0] * linha
print(matriz)
for l in range(len(matriz)):
    matriz[l] = [0] * coluna
# ler as linhas
for l in range(len(matriz)):
    # ler as colunas
    for c in range(len(matriz[l])):
        matriz[l][c] = l * c
for l in range(len(matriz)):
    print(matriz[l])
