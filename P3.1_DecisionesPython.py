print("3.1 Como tomar decisiones en Python")

print()
print("3.1.1 Preguntas y respuestas")
print("Python puede comparar valores y responder con True o False.")

print()
print("Operador de igualdad ==")
print(2 == 2)
print(2 == 2.0)
print(1 == 2)

print()
print("Operador de desigualdad !=")
var = 0
print(var != 0)

var = 1
print(var != 0)

print()
print("Operador mayor que >")
print(5 > 2)
print(2 > 5)

print()
print("Operador mayor o igual que >=")
print(5 >= 5)
print(4 >= 5)

print()
print("Operador menor que <")
print(3 < 8)
print(9 < 2)

print()
print("Operador menor o igual que <=")
print(3 <= 3)
print(7 <= 4)

print()
print("Guardar respuestas en variables")
answer = 10 >= 5
print(answer)

print()
print("3.1.7 Condiciones y ejecucion condicional")
x = 10

if x == 10:
    print("x es igual a 10")

if x > 5:
    print("x es mayor que 5")

if x < 10:
    print("x es menor que 10")
else:
    print("x no es menor que 10")

print()
print("if - else")
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print()
print("if - elif - else")
calificacion = 85

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
else:
    print("Reprobado")

print()
print("Comparar 3 numeros")
number1 = 5
number2 = 10
number3 = 8

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("El numero mas grande es:", largest_number)

print()
print("Ejemplo con cadenas")
planta = "espatifilo"

if planta == "ESPATIFILO":
    print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif planta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No", planta + "!")

print()
print("Ejemplo de anio bisiesto")
year = 2000

if year < 1582:
    print("No dentro del periodo del calendario gregoriano")
elif year % 4 != 0:
    print("Año comun")
elif year % 100 != 0:
    print("Año bisiesto")
elif year % 400 != 0:
    print("Año comun")
else:
    print("Año bisiesto")