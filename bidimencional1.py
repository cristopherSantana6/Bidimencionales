# Crear una matriz 4x3 para almacenar las calificaciones
calificaciones = [
    [85, 90, 88],   
    [78, 82, 80],  
    [92, 88, 91],   
    [70, 75, 73]]

# Calcular y mostrar el promedio de cada materia
print("Promedios por materia:")
for i in range(4):
    suma = sum(calificaciones[i])
    promedio = suma / 3
    print(f"Materia {i + 1}: {promedio:.2f}")

# Encontrar la calificación más alta de toda la matriz
mayor = calificaciones[0][0]
for fila in calificaciones:
    for nota in fila:
        if nota > mayor:
            mayor = nota

print(f"\nLa calificación más alta de toda la matriz es: {mayor}")
