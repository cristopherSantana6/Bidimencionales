n = int(input("Número de filas (n < 10): "))
m = int(input("Número de columnas (m < 10): "))

# Crear matriz
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Valor en [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# c. Suma por fila
print("\nSuma por fila:")
for i, fila in enumerate(matriz):
    print(f"Fila {i+1}: {sum(fila)}")

# d. Promedio por columna
print("\nPromedio por columna:")
for j in range(m):
    suma_col = sum(matriz[i][j] for i in range(n))
    print(f"Columna {j+1}: {suma_col/n:.2f}")

# e. Mayor valor y su ubicación
mayor = matriz[0][0]
fila_mayor = columna_mayor = 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            fila_mayor, columna_mayor = i, j
print(f"\nMayor valor: {mayor} en fila {fila_mayor}, columna {columna_mayor}")