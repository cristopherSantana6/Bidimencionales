# Solicitar filas (n) y columnas (m) válidas (<10)
while True:
    n = int(input("Ingrese el número de filas (menor que 10): "))
    m = int(input("Ingrese el número de columnas (menor que 10): "))
    if 1 <= n < 10 and 1 <= m < 10:
        break
    else:
        print("⚠️ Error: Ambos valores deben ser mayores que 0 y menores que 10.\n")

# Captura de los valores de la matriz con validación
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        while True:
            valor = int(input(f"Ingrese valor para M[{i}][{j}] (0-9): "))
            if 0 <= valor < 10:
                fila.append(valor)
                break
            else:
                print("Error: Ingrese un número entre 0 y 9.")
    matriz.append(fila)

# Suma por fila
print("\n📌 Suma por fila:")
for i, fila in enumerate(matriz):
    print(f"Fila {i+1}: {sum(fila)}")

# Promedio por columna
print("\n📌 Promedio por columna:")
for j in range(m):
    promedio = sum(matriz[i][j] for i in range(n)) / n
    print(f"Columna {j+1}: {promedio:.2f}")

# Mayor valor y su posición
mayor = matriz[0][0]
fila_m, col_m = 0, 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor, fila_m, col_m = matriz[i][j], i, j
print(f"\n🔍 Mayor valor: {mayor}, ubicado en fila {fila_m}, columna {col_m}")