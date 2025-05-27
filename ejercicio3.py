matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Linealización por columnas
filas = len(matriz)
columnas = len(matriz[0])
lineal = []

for columna in range(columnas):
    for fila in range(filas):
        lineal.append(matriz[fila][columna])

print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nArreglo linealizado por columnas:")
print(lineal)