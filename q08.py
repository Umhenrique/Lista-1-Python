from q04 import matriz_comando

#Declaração de variaveis

multi_linha_1 = []
multi_linha_2 = []
matriz_final = []

#Atribuição de Valores
print("Insira os valores da matriz 2 X 2")
matriz_A = matriz_comando(2, 2)
print("Insira os valores da matriz 2 X 1")
matriz_B = matriz_comando(2, 1)

#Efetuar a multiplicação


multi_linha_1.append((matriz_A[0][0] * matriz_B [0][0]) + ((matriz_A[0][1] * matriz_B [1][0])))
multi_linha_2.append((matriz_A[1][0] * matriz_B [0][0]) + ((matriz_A[1][1] * matriz_B [1][0])))

matriz_final.append(multi_linha_1)
matriz_final.append(multi_linha_2)

#Apresentação do resultado

print("O valor da multiplicação da matrizes é ! ")
print("-", " " * len(str(matriz_final[0][0])), "-")
for k in range(2):
    print("|", matriz_final[k][0], "|")
print("-", " " * len(str(matriz_final[1][0])), "-")