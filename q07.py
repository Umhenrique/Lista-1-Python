#Atribuição de Valores

q_linha_matriz_A = int(input("insira a quantidade de linhas que deve ter a matriz A: "))
q_colunas_matriz_A = int(input("Insira a quantidade de colunas que deve ter a matriz A: "))

q_linha_matriz_B = int(input("insira a quantidade de linhas que deve ter a matriz B: "))
q_colunas_matriz_B = int(input("Insira a quantidade de colunas que deve ter a matriz B: "))

if q_colunas_matriz_A == q_linha_matriz_B:
    print("É possivel efetuar a multiplicação de matrizes")
else:
    print("A multiplicação de matrizes não pode ser efetuada, por favor re informe os valores")
    exit()