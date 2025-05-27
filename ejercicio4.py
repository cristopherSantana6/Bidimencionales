n = int(input("Filas (<10): "))
m = int(input("Columnas (<10): "))

# Captura de matriz
matriz = [[int(input(f"M[{i}][{j}]: ")) for j in range(m)] for i in range(n)]

# Suma por fila
print("\nSuma por fila:")
for i, fila in enumerate(matriz):
    print(f"Fila {i+1}: {sum(fila)}")

# Promedio por columna
print("\nPromedio por columna:")
for j in range(m):
    promedio = sum(matriz[i][j] for i in range(n)) / n
    print(f"Columna {j+1}: {promedio:.2f}")

# Mayor valor y posición
mayor = matriz[0][0]
fila_m, col_m = 0, 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor, fila_m, col_m = matriz[i][j], i, j
print(f"\nMayor valor: {mayor} en fila {fila_m}, columna {col_m}")