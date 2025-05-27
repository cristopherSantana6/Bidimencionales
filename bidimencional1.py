ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 90000, 85000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

# a. Venta total de todas las tiendas
total_general = sum(sum(tienda) for tienda in ventas)

# b. Venta total por tienda
totales_por_tienda = [sum(tienda) for tienda in ventas]

# c. Tienda que más vendió
tienda_mayor = totales_por_tienda.index(max(totales_por_tienda)) + 1

# d. Tienda que menos vendió
tienda_menor = totales_por_tienda.index(min(totales_por_tienda)) + 1

print(f"Venta total en todas las tiendas: {total_general}")
for i, total in enumerate(totales_por_tienda, start=1):
    print(f"Total ABSA {i}: {total}")
print(f"Tienda que más vendió: ABSA {tienda_mayor}")
print(f"Tienda que menos vendió: ABSA {tienda_menor}")
