print("4.1 Funciones")

print()
print("4.1.1 ¿Por que necesitamos funciones?")
print("Las funciones ayudan a reutilizar codigo.")
print("Tambien hacen que el programa sea mas ordenado y facil de leer.")

print()
print("Ejemplo sin funcion")
print("Ingresar valor:")
print("Ingresar valor:")
print("Ingresar valor:")

print()
print("4.1.4 Tu primera funcion")

def message():
    print("Ingresar valor:")

print("Inicia aqui.")
print("Termina aqui.")

print()
print("Invocando la funcion")
print("Inicia aqui.")
message()
print("Termina aqui.")

print()
print("Llamando la funcion varias veces")
message()
message()
message()

print()
print("4.1.5 Como funcionan las funciones")
print("Python ejecuta la funcion solo cuando se invoca.")

def hello():
    print("Hello")

hello()

print()
print("Funcion mezclada con codigo normal")
print("Comienza aqui.")

def saludo():
    print("Hola desde una funcion")

saludo()
print("Termina aqui.")

print()
print("Usando una funcion para evitar repetir codigo")

def pedir_valor():
    print("Por favor, ingresar valor:")

pedir_valor()
a = 10
print("a =", a)

pedir_valor()
b = 20
print("b =", b)

pedir_valor()
c = 30
print("c =", c)

print()
print("Valores finales")
print(a, b, c)

print()
print("Funcion con un parametro")

def hi(name):
    print("Hello,", name)

hi("Saulo")
hi("Python")

print()
print("Prueba de seccion")

print()
print("Pregunta 1")
print("input() es una funcion integrada")

print()
print("Pregunta 2")
print("Llamar una funcion antes de definirla produce NameError")

print()
print("Pregunta 3")
print("Llamar una funcion con argumentos incorrectos produce TypeError")