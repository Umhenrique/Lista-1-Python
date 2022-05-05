def matriz_comando(linha_matriz, coluna_matriz):
    matriz = []
    for linhas in range(linha_matriz):
        valores_matriz = []
        for colunas in range(coluna_matriz):
            valor = int(input(f"digite as linhas[{linhas + 1}]colunas[{colunas + 1}] da matriz: "))
            valores_matriz.append(valor)
        matriz.append(valores_matriz)
    return matriz
