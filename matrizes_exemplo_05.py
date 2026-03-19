#4 - Leia uma matriz 4 x 4,
# imprima a matriz e retorne a localização
# (linha e a coluna) do maior valor.
from random import randint
valor_maior = 0
pos_1 = 0
pos_2 = 0
linha = int(input("Digite a quantidade de "
                  "linhas da matriz \t"))
coluna = int(input("Digite a quantidade de "
                   "colunas da matriz \t"))
matriz = [0] * linha
for l in range(len(matriz)):
    matriz[l] = [0] * coluna

valor_maior = matriz[0][0]
# ler as linhas
for k in range(len(matriz)):
  #ler as colunas
    for m in range(len(matriz[k])):
        matriz[k][m] = randint(1,100)  #int(input("Digite o valor \t"))
        if matriz[k][m] >= valor_maior:
            valor_maior = matriz[k][m]
            pos_1 = k
            pos_2 = m
#print(matriz)
for l in range(len(matriz)):
    print(matriz[l])
print("O valor é:", valor_maior)
print("na linha e coluna", pos_1, pos_2)
