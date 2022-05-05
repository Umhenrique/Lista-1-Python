from q04 import matriz_comando

#Declaração de variaveis

multi_linha_1 = []
multi_linha_2 = []
matriz_final = []

#Atribuição de Valores

escalar = int(input("Insira o valor da Escalar que você deseja utilizar: "))
q_linha_matriz = int(input("insira a quantidade de linhas que deve ter a matriz: "))
if q_linha_matriz != 2:
    print("As linhas não podem ter um valor diferente de 2")
    exit()
q_colunas_matriz = int(input("Insira a quantidade de colunas que deve ter a matriz: "))
if q_colunas_matriz != 2:
    print("As colunas não podem ter o valor diferente de 2")
    exit()
matriz = matriz_comando(q_linha_matriz, q_colunas_matriz)

#Efetuar a multiplicação

for j in range(2):
    multi_linha_1.append(matriz[0][j] * escalar)
    multi_linha_2.append(matriz[1][j] * escalar)
matriz_final.append(multi_linha_1)
matriz_final.append(multi_linha_2)

#Apresentação do resultado

print("O valor da multiplicação da matrizes é ! ")
print("-", " " * (len(str(matriz_final[0][0])) + len(str(matriz_final[0][1])))," " "-")
for k in range(2):
    print("|", matriz_final[k][0], matriz_final[k][1], "|")
print("-", " " * (len(str(matriz_final[1][0])) + len(str(matriz_final[1][1])))," " "-")