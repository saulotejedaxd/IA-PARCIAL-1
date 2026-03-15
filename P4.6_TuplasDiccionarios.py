print("4.6 Tuplas y diccionarios")

print()
print("4.6.1 Tipos de secuencia y mutabilidad")
print("Las listas son mutables")
print("Las tuplas son inmutables")

print()
print("4.6.2 Tuplas")
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1.0, 0.5, 0.25, 0.125

print(tuple_1)
print(tuple_2)

print()
print("Tupla vacia")
empty_tuple = ()
print(empty_tuple)

print()
print("Tupla de un solo elemento")
one_element_tuple_1 = (1,)
one_element_tuple_2 = 1.,
print(one_element_tuple_1)
print(one_element_tuple_2)

print()
print("Acceso a elementos de una tupla")
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])

print()
print("Recorrer una tupla")
for elem in my_tuple:
    print(elem)

print()
print("Operaciones con tuplas")
print(len(my_tuple))
print(my_tuple + (10000,))
print((1, 10, 100) * 3)
print(10 in my_tuple)
print(5 not in my_tuple)

print()
print("Intercambio de tuplas")
var = 123
t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

print()
print("4.6.3 Diccionarios")
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {"jefe": 5551234567, "Suzy": 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print()
print("Acceso a valores del diccionario")
print(dictionary["gato"])
print(phone_numbers["Suzy"])

print()
print("Uso de in y not in")
words = ["gato", "leon", "caballo"]

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no esta en el diccionario")

print()
print("4.6.4 Metodos de diccionarios")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()
for spanish, french in dictionary.items():
    print(spanish, "->", french)

print()
for french in dictionary.values():
    print(french)

print()
print("Modificar valores")
dictionary["gato"] = "minou"
print(dictionary)

print()
print("Agregar nuevas claves")
dictionary["cisne"] = "cygne"
print(dictionary)

dictionary.update({"pato": "canard"})
print(dictionary)

print()
print("Eliminar claves")
del dictionary["perro"]
print(dictionary)

dictionary.popitem()
print(dictionary)

print()
print("Ordenar claves")
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

print()
print("4.6.5 Tuplas y diccionarios juntos")
school_class = {}

school_class["Bob"] = (7, 2, 9)
school_class["Andy"] = (3, 10, 3)

for name in sorted(school_class.keys()):
    total = 0
    counter = 0
    for grade in school_class[name]:
        total += grade
        counter += 1
    print(name, ":", total / counter)

print()
print("Prueba de seccion")

print()
print("Pregunta 1")
my_tup = (1, 2, 3)
print(my_tup[2])

print()
print("Pregunta 2")
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)

print()
print("Pregunta 3")
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)

print()
print("Pregunta 4")
d1 = {"Adam Smith": "A", "Judy Paxton": "B+"}
d2 = {"Mary Louis": "A", "Patrick White": "C"}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

print()
print("Pregunta 5")
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)
print(t)

print()
print("Pregunta 6")
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)

print()
print("Pregunta 7")
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)

print()
print("Pregunta 8")
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)