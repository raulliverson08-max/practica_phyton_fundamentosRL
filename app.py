#   comentario de una sola linea
"""
    Comentario multilinea
"""
print("hola mundo desde python")

# Escribe un codigo en python que me permita hacer la suma 2 numeros
"""
Entrada:
    solicitar 2 numeros 
Proceso
    hacer la operacion de matematicas
Salida
    mostrar el resultado
"""
# Entrada
numero_1 = 2
numero_2 = 3
# Proceso
suma = numero_1 + numero_2
# Salida
print("El resultado de la suma es:", suma)


# Escribe un programa que me permita saber si un alumno aprueba o reprueba un curso
"""
Nota minima para aprobar: 4
Entrada:
    solicitar la nota del alumno
Proceso:
    comparar la nota con la nota minima
Salida:
    mostrar si aprueba o reprueba el curso
"""
nota_1 = 6
nota_2 = 1
nota_3 = 4
nota_minima = 4

suma_notas = nota_1 + nota_2 + nota_3
promedio = suma_notas / 3

if promedio >= nota_minima:
    print("El alumno aprueba el curso con un promedio de:", promedio)
else:
    print("El alumno reprueba el curso con un promedio de:", promedio)

# Escribe un programa que me permita saber si un numero es par o impar
"""
Entrada
    Buscar en una lista de numeros que nuemero son pares y cuales son impares
Proceso
    validar si el numero es par o impar
Salida
    mostrar los numeros pares e impares
"""
"""
estructura de un bucle for
for variable in secuencia:
    bloque de codigo a ejecutar


Forma de agregar elementos dentro de una lista
lista.append(elemento)
"""


# lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:
        print("El numero", numero, "es par")
        print(f"El numero {numero} es par")
        numeros_pares.append(numero)
    else:
        print("El numero", numero, "es impar")
        print(f"El numero {numero} es impar")
        numeros_impares.append(numero)
print("Numeros pares:", numeros_pares)
print("Numeros impares:", numeros_impares)