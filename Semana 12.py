import random

# Definir ciudades y semanas
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 2  # Número de semanas

# Crear una matriz tridimensional para almacenar temperaturas
# Dimensiones: [ciudad][día][semana]
temperaturas = [[[random.uniform(10, 30) for _ in range(7)] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar el promedio de temperaturas por ciudad y por semana
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas promedio para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(7):
            suma_temperaturas += temperaturas[i][semana][dia]
        promedio = suma_temperaturas / 7
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")
