matriz = [
          [5.6, 7.9, 8.6,9.9],
          [5.5, 2.2, 8.7,7.8],
          [4.4, 9.8, 9.9, 5.1]
          ]
#leitura da matriz 
for l in range(len(matriz)):
    print(matriz[l])
# ler linhas
for l in range(len(matriz)):
    # ler colunas
    for c in range(len(matriz[l])):
        print("O valor da linha ", l, "coluna "
              , c, "e: ", matriz[l][c])
print(matriz)

