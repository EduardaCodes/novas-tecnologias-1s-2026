def transpor_matriz(matriz):
    transposta = []
    
    for j in range(len(matriz[0])):
        linha = []
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
        transposta.append(linha)
    
    return transposta


def multiplicar_matriz(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        return None
    
    resultado = []
    
    for i in range(len(matriz_a)):
        linha = []
        for j in range(len(matriz_b[0])):
            soma = 0
            for k in range(len(matriz_b)):
                soma += matriz_a[i][k] * matriz_b[k][j]
            linha.append(soma)
        resultado.append(linha)
    
    return resultado