print("4.2 Parametros en funciones")

print()
print("Funcion con un parametro")

def message(number):
    print("Ingresa un numero:", number)

message(1)
message(5)

print()
print("Variable y parametro con el mismo nombre")

def show(number):
    print("Dentro de la funcion:", number)

number = 1234
show(7)
print("Fuera de la funcion:", number)

print()
print("Funcion con dos parametros")

def message2(what, number):
    print("Ingresa", what, "numero", number)

message2("telefono", 11)
message2("precio", 5)

print()
print("Argumentos posicionales")

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

print()
print("Argumentos con palabra clave")

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")

print()
print("Mezcla de argumentos")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(3, c=1, b=2)

print()
print("Valores por defecto")

def intro_default(first_name, last_name="Gonzalez"):
    print("Hola, mi nombre es", first_name, last_name)

intro_default("Enrique")
intro_default("Jorge", "Perez")
intro_default(first_name="Guillermo")

print()
print("Dos valores por defecto")

def intro_full(first_name="Juan", last_name="Gonzalez"):
    print("Hola, mi nombre es", first_name, last_name)

intro_full()
intro_full(last_name="Rodriguez")

print()
print("Prueba de seccion")

print()
print("Pregunta 1")
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro()

print()
print("Pregunta 2")
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sean Connery")

print()
print("Pregunta 3")
def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro("Susan")

print()
print("Pregunta 4")
print("def add_numbers(a, b=2, c):")
print("Ese codigo es incorrecto")
print("porque c no puede ir despues de un parametro con valor por defecto")