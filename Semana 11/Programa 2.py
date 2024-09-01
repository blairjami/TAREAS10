# Crear una matriz bidimensional de 3x3
matriz = [
    [3, 2, 1],
    [9, 8, 7],
    [6, 5, 4]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir la fila a ordenar
fila_a_ordenar = 1

# Ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
