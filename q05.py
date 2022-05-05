from q04 import matriz_comando

#Declaração de variaveis

lista_matriz_soma = []
soma_linha_1 = []
soma_linha_2 = []

#As linhas recebem os valores
print("Insira os valores da primeira matriz 2 X 2")
lista_matriz_1 = matriz_comando(2, 2)
print("Insira os valores da segunda matriz 2 X 2")
lista_matriz_2 = matriz_comando(2, 2)

#Soma

for j in range(2):
    soma_linha_1.append(lista_matriz_1[0][j] + lista_matriz_2[0][j])
    soma_linha_2.append(lista_matriz_1[1][j] + lista_matriz_2[1][j])

#Acrescento as duas listas em uma terceira matriz

lista_matriz_soma.append(soma_linha_1)
lista_matriz_soma.append(soma_linha_2)

#Apresentação do resultado

print("O valor da soma das matrizes é ! ")
print("-", " " * (len(str(lista_matriz_soma[0][0])) + len(str(lista_matriz_soma[0][1])))," " "-")
for k in range(2):
    print("|", lista_matriz_soma[k][0], lista_matriz_soma[k][1], "|")
print("-", " " * (len(str(lista_matriz_soma[1][0])) + len(str(lista_matriz_soma[1][1])))," " "-")
