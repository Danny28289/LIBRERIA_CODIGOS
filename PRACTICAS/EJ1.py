def ordenar_matriz(N):
    # Creación de la matriz NxN
    matriz = [[0] * N for _ in range(N)]
    # Función auxiliar para imprimir la matriz
    def imprimir_matriz(mat):
        for i in range(N):
            for j in range(N):
                print(mat[i][j], end="\t")
            print()
        print()
    # Llenar la matriz con los valores del ejemplo
    # Primera fila
    matriz[0] = [5, 40, 13, 32, 1]
    matriz[1] = [10, 37, 25, 50, 10]
    matriz[2] = [15, 2, 13, 26, 1]
    matriz[3] = [2, 19, 45, 7, 16]
    matriz[4] = [13, 28, 11, 45, 13]
    
    print("Matriz original:")
    imprimir_matriz(matriz)
    
    # Ordenar cada fila usando ordenamiento burbuja
    for fila in range(N):
        for i in range(N):
            for j in range(0, N - i - 1):
                if matriz[fila][j] > matriz[fila][j + 1]:
                    # Intercambiar elementos
                    temp = matriz[fila][j]
                    matriz[fila][j] = matriz[fila][j + 1]
                    matriz[fila][j + 1] = temp
    print("Matriz ordenada por filas:")
    imprimir_matriz(matriz)
    return matriz
# Ejecutar el programa con N=5 (según el ejemplo)
matriz_ordenada = ordenar_matriz(5)