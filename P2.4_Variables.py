print("2.4 Variables")

print()
print("2.4.1 Variables - cajas con forma de datos")
print("Una variable es una caja donde se puede guardar informacion.")
print("Cada variable tiene un nombre y un valor.")

print()
print("2.4.2 Nombres de variables")
print("Reglas basicas:")
print("Deben comenzar con letra o guion bajo.")
print("Pueden tener letras, numeros y guion bajo.")
print("No pueden tener espacios.")
print("No pueden ser palabras reservadas.")
print("Python distingue entre mayusculas y minusculas.")

print()
print("Ejemplos de nombres correctos:")
print("my_variable")
print("contador")
print("total_apples")
print("_dato")
print("m101")

print()
print("Ejemplos de nombres incorrectos:")
print("101")
print("m 101")
print("del")

print()
print("2.4.3 Como crear una variable")
var = 1
print("Se creo la variable var con valor de:")
print(var)

print()
print("2.4.4 Como emplear una variable")
x = 10
y = 5
print("Valor de x:")
print(x)
print("Valor de y:")
print(y)
print("Suma de x + y:")
print(x + y)

print()
print("Combinar texto con variables")
version = "3.12.3"
print("Python version: " + version)

print()
print("2.4.5 Como asignar un nuevo valor a una variable ya existente")
var = 1
print("Valor inicial de var:")
print(var)

var = var + 1
print("Nuevo valor de var despues de sumarle 1:")
print(var)

print()
var = 100
var = 200 + 300
print("Nuevo valor de var:")
print(var)

print()
print("2.4.6 Resolviendo problemas matematicos simples")
print("Teorema de Pitagoras")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("a =", a)
print("b =", b)
print("c =", c)

print()
print("2.4.7 LAB Variables")
john = 3
mary = 5
adam = 6

print("Manzanas de cada persona:")
print(john, mary, adam)

total_apples = john + mary + adam
print("Total de manzanas:")
print(total_apples)

print("Numero total de manzanas:", total_apples)

print()
print("Operaciones con variables")
print("john + mary =")
print(john + mary)

print("adam - john =")
print(adam - john)

print("mary * 2 =")
print(mary * 2)

print("adam / 2 =")
print(adam / 2)

print("adam // 2 =")
print(adam // 2)

print()
print("2.4.8 Operadores abreviados")
x = 5
print("Valor inicial de x:")
print(x)

x += 3
print("x += 3")
print(x)

x -= 2
print("x -= 2")
print(x)

x *= 4
print("x *= 4")
print(x)

x /= 2
print("x /= 2")
print(x)

print()
sheep = 10
print("Sheep inicial:")
print(sheep)

sheep += 1
print("Sheep despues de += 1")
print(sheep)

print()
print("2.4.9 LAB Variables: un convertidor simple")
miles = 7.38
kilometers = miles * 1.61
print(miles, "millas son", round(kilometers, 2), "kilometros")

kilometers = 12.25
miles = kilometers / 1.61
print(kilometers, "kilometros son", round(miles, 2), "millas")

print()
print("2.4.10 LAB Operadores y expresiones")
x = 0.0
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("x =", x)
print("y =", y)

print()
x = 1.0
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("x =", x)
print("y =", y)

print()
x = -1.0
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("x =", x)
print("y =", y)

print()
print("2.4.12 Cuestionario de seccion")

print()
print("Pregunta 1")
var = 2
var = 3
print(var)

print()
print("Pregunta 3")
a = '1'
b = "1"
print(a + b)

print()
print("Pregunta 4")
a = 6
b = 3
a /= 2 * b
print(a)
