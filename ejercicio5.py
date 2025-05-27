# Ventas de 3 vendedores en 4 zonas
ventas = [
    [5, 3, 7, 4],   # Vendedor 1
    [2, 6, 1, 5],   # Vendedor 2
    [4, 2, 8, 6]    # Vendedor 3
]

# a. Zona con más computadoras vendidas
zonas = [sum(ventas[i][j] for i in range(3)) for j in range(4)]
print(f"a. Zona con más ventas: Zona {zonas.index(max(zonas))+1}")

# b. Vendedor con menos computadoras vendidas
vendedores = [sum(fila) for fila in ventas]
print(f"b. Vendedor con menos ventas: Vendedor {vendedores.index(min(vendedores))+1}")

# c. Total de ventas
total = sum(sum(fila) for fila in ventas)
print(f"c. Total de computadoras vendidas: {total}")