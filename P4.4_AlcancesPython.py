print("4.4 Alcances en Python")

print()
print("4.4.1 Funciones y alcances")
var = 1

def my_function():
    print("¿Conozco a la variable?", var)

my_function()
print(var)

print()
print("Variable local y variable global con el mismo nombre")

def my_function_local():
    var = 2
    print("¿Conozco a la variable?", var)

var = 1
my_function_local()
print(var)

print()
print("Una variable local solo existe dentro de la funcion")

def adding(x):
    var = 7
    return x + var

print(adding(4))

print()
print("4.4.2 Palabra clave global")
var = 2
print("Antes de la funcion:", var)

def return_var():
    global var
    var = 5
    return var

print("Valor devuelto:", return_var())
print("Despues de la funcion:", var)

print()
print("Otro ejemplo con global")
a = 1

def fun_global():
    global a
    a = 2
    print("Dentro de fun_global:", a)

fun_global()
print("Fuera de fun_global:", a)

print()
print("4.4.3 Interaccion con argumentos escalares")

def my_function_arg(n):
    print("Yo recibi", n)
    n += 1
    print("Ahora tengo", n)

var = 1
my_function_arg(var)
print(var)

print()
print("Interaccion con listas")

def my_function_list(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function_list(my_list_2)
print("Print #5:", my_list_2)

print()
print("Modificar la lista identificada por el parametro")

def my_function_list2(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function_list2(my_list_2)
print("Print #5:", my_list_2)

print()
print("Resumen rapido")

var = 2
def mult_by_var(x):
    return x * var

print(mult_by_var(7))

def mult(x):
    var = 5
    return x * var

print(mult(7))

def mult2(x):
    var = 7
    return x * var

var = 3
print(mult2(7))

print()
print("Prueba de seccion")

print()
print("Pregunta 1")
def message():
    alt = 1
    print("¡Hola, mundo!")

print("print(alt) daria NameError porque alt solo existe dentro de message")

print()
print("Pregunta 2")
a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)

print()
print("Pregunta 3")
a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)

print()
print("Pregunta 4")
a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)