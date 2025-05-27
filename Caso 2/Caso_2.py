# Programa para capturar el nombre y tres calificaciones de 5 estudiantes,
# calcular el promedio final de cada uno y mostrarlo en pantalla,
# utilizando un arreglo bidimensional para almacenar los datos.
# No se utilizan funciones; todo está secuenciado linealmente.

# Número total de estudiantes
num_estudiantes = 5
# Número de calificaciones por estudiante
num_calificaciones = 3

# Crear arreglo bidimensional llamado 'estudiantes' con 5 filas y 4 columnas:
# Columnas: 0 -> nombre (string), 1 a 3 -> calificaciones (float)
# Se inicializa con cadenas vacías para nombres y ceros para calificaciones
estudiantes = [["" for _ in range(num_calificaciones + 1)] for _ in range(num_estudiantes)]

print("Captura de nombres y calificaciones para 5 estudiantes:")

# Ciclo para capturar datos de cada estudiante
for i in range(num_estudiantes):
    print(f"\nDatos Estudiante {i + 1}:")
    # Capturar y almacenar el nombre en la columna 0
    estudiantes[i][0] = input("Ingrese el nombre: ").strip()

    # Capturar las tres calificaciones en columnas 1 a 3
    for j in range(1, num_calificaciones + 1):
        while True:
            try:
                calif = float(input(f"Calificación {j} (0 a 100): "))
                # Validar que la calificación esté en el rango correcto
                if 0 <= calif <= 100:
                    # Almacenar la calificación en el arreglo
                    estudiantes[i][j] = calif
                    break  # Salir del ciclo mientras para esta calificación
                else:
                    print("Error: La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada inválida: ingrese un número válido para la calificación.")

# Mostrar el resultado: promedio final de cada estudiante
print("\nPromedio final de los estudiantes:")
for i in range(num_estudiantes):
    nombre = estudiantes[i][0]
    # Extraer calificaciones para calcular promedio
    calificaciones = estudiantes[i][1:]
    promedio = sum(calificaciones) / num_calificaciones
    # Mostrar el nombre y promedio con dos decimales
    print(f"{nombre}: {promedio:.2f}")

