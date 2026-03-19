linha = int(input("Digite a quantidade "
                  "de linhas da matriz \t"))
coluna = int(input("Digite a quantidade "
                   "de colunas da matriz \t"))
matriz = [int] * linha
for l in range(len(matriz)):
    matriz[l] = [int] * coluna
print("")
# ler as linhas
for l in range(len(matriz)):
  #ler as colunas
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Digite o valor \t"))
        if l ==c: 
            print("Elemento da diagonal principal",
                  matriz[l][c])
print("")
for l in range(len(matriz)):
    print(matriz[l])
print("")
print(matriz)
