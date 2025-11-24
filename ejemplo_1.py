"""
Escriba un programa en python que me permita seleccionar productos de un menu calcular su precio total e imprimir una factura. 
El menu debe tener al menos 5 productos con sus respectivos precios. 
El usuario debe poder seleccionar multiples productos y cantidades. 
Al final, el programa debe mostrar un resumen de la compra con el total a pagar.
"""

"""
Entrada:
    - mostrarle al usuario un menu con 5 productos y sus precios
    - permitirle seleccionar multiples productos y cantidades

Proceso:
    - calcular el precio total de los productos seleccionados
    - generar un resumen de la compra

Salida:
    - imprimir la factura con el resumen de la compra y el total a pagar

"""

"""
Notas:
Estructura a utilizar:
- Diccionario para almacenar productos y precios
- Bucle para permitir multiples selecciones
- Formateo de salida para la factura
"""

"""
Array en js 
    => array = [1,2,3,4,5]
lista en python
    => lista = [1,2,3,4,5]
array asociativo en js
    => array = { 
        "producto1": 10, 
        "producto2": 20 
    }
diccionario en python
    => diccionario = { 
        "producto1": 10, 
        "producto2": 20 
    }
"""
# Ejemplo de lista en python
lista_objetos = ["pelota", "muñeca", "carro", "rompecabezas", "juego de mesa"]
# indices:        0         1        2         3               4 
#ejemplo
print(lista_objetos[2])
print("--------------------")


# Ejemplo de diccionario en python
clientes = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Madrid",
    "telefono": "123456789",
    "email": "juan.perez@example.com"
}
# Accediendo a los valores del diccionario
print(clientes["nombre"])
print("--------------------")

# Acceder a los valores de la lista dentro de un bucle
for i in range(len(lista_objetos)):
    print(f"El objeto en el indice {i} es: {lista_objetos[i]}")

print("--------------------")

# Acceder a los valores del diccionario dentro de un bucle
for clave in clientes:
    print(f"La clave es: {clave} y el valor es: {clientes[clave]}")



