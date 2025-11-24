"""
Operadores de comparación en Python
or ( cuando al menos una condicion es verdadera)
and ( cuando todas las condiciones son verdaderas)
== : Igual a
!= : Diferente de
>  : Mayor que
<  : Menor que
>= : Mayor o igual que
<= : Menor o igual que
"""
# ejemplo con el operador OR
a = 5
b = 3
c = 8
if a > b or a > c:
    print(f"{a} es mayor que {b} o {c}")
else:
    print(f"{a} no es mayor que {b} ni {c}")
print("--------------------------------------------------")
# ejemplo con el operador AND
if a > b and c > a:
    print(f"{a} es mayor que {b} y {c} es mayor que {a}")
else:
    print(f"Una de las condiciones no se cumple")
print("--------------------------------------------------")

# ejemplo con el operador ==
x = 10
y = 10
if x == y:
    print(f"{x} es igual a {y}")
else:
    print(f"{x} no es igual a {y}")
print("--------------------------------------------------")
# ejemplo con el operador !=
if x != b:
    print(f"{x} es diferente de {b}")
else:
    print(f"{x} es igual a {b}")
print("--------------------------------------------------")
# ejemplo con el operador >
if c > a:
    print(f"{c} es mayor que {a}")
else:
    print(f"{c} no es mayor que {a}")
print("--------------------------------------------------")
# ejemplo con el operador <
if b < a:
    print(f"{b} es menor que {a}")
else:
    print(f"{b} no es menor que {a}")
print("--------------------------------------------------")
# ejemplo con el operador >=
if a >= b:
    print(f"{a} es mayor o igual que {b}")
else:
    print(f"{a} no es mayor o igual que {b}")
print("--------------------------------------------------")
# ejemplo con el operador <=
if b <= a:
    print(f"{b} es menor o igual que {a}")
else:
    print(f"{b} no es menor o igual que {a}")
print("--------------------------------------------------")


