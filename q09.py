from q04 import matriz_comando

#Declaração de variaveis

matriz_c = []
soma_linha_1 = []
soma_linha_2 = []
soma_linha_3 = []

#As linhas recebem os valores
print("Insira os valores da primeira matriz 2 X 3")
matriz_A = matriz_comando(2, 3)
print("Insira os valores da segunda matriz 3 X 2")
matriz_B = matriz_comando(3, 2)

#Multiplicaçãp
for j in range (2):
    soma_linha_1.append((matriz_A[0][0] * matriz_B[0][j]) + (matriz_A[0][1] * matriz_B[1][j]) + (matriz_A[0][2] * matriz_B[2][j]))
    soma_linha_2.append((matriz_A[1][0] * matriz_B[0][j]) + (matriz_A[1][1] * matriz_B[1][j]) + (matriz_A[1][2] * matriz_B[2][j]))

#Acrescento as duas listas em uma terceira matriz

matriz_c.append(soma_linha_1)
matriz_c.append(soma_linha_2)

#Apresentação do resultado

print("O valor da soma das matrizes é ! ")
print("-", " " * (len(str(matriz_c[0][0])) + len(str(matriz_c[0][1]))), " " "-")
for k in range(2):
    print("|", matriz_c[k][0], matriz_c[k][1], "|")
print("-", " " * (len(str(matriz_c[1][0])) + len(str(matriz_c[1][1]))), " " "-")
