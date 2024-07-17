# Realice y represente mediante diagrama de flujo y pseudocódigo un
# algoritmo que lea los nombres y las edades de diez alumnos, y que los
# datos se almacenen en dos vectores, y con base en esto se determine
# el nombre del alumno con la edad mayor del arreglo.

alumnos = [[], []]
for i in range(10):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    alumnos[0].append(nombre)
    alumnos[1].append(edad)

edad_max = -1
nombre_edad_max = ""

for i in range(10):
    if alumnos[1][i] > edad_max:
        edad_max = alumnos[1][i]
        nombre_edad_max = alumnos[0][i]

print(f"\nEl alumno con la mayor edad es {nombre_edad_max} con {edad_max} años.")
