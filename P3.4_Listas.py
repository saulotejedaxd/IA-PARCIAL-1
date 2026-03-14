print("3.4 Listas")

print()
print("3.4.1 Crear una lista")
numbers = [10, 5, 7, 2, 1]
print(numbers)

print()
print("3.4.2 Indexacion de listas")
print("Primer elemento:", numbers[0])
print("Ultimo elemento:", numbers[4])

numbers[0] = 111
print("Lista modificada:", numbers)

numbers[1] = numbers[4]
print("Copiando el quinto al segundo:", numbers)

print()
print("3.4.3 Acceso y longitud")
print(numbers)
print("Longitud de la lista:", len(numbers))

print()
print("3.4.4 Eliminar elementos")
del numbers[1]
print("Lista despues de eliminar:", numbers)
print("Nueva longitud:", len(numbers))

print()
print("3.4.5 Indices negativos")
print("Ultimo elemento:", numbers[-1])
print("Penultimo elemento:", numbers[-2])

print()
print("3.4.6 Fundamentos de listas")
hat_list = [1, 2, 3, 4, 5]
hat_list[2] = int(input("Ingresa un numero para reemplazar el valor central: "))
del hat_list[-1]
print("Longitud de la lista:", len(hat_list))
print(hat_list)

print()
print("3.4.8 append() e insert()")
my_list = []

for i in range(5):
    my_list.append(i + 1)

print("Con append:", my_list)

my_list.insert(0, 100)
print("Con insert al inicio:", my_list)

print()
print("3.4.9 Recorrer lista y sumar")
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print("Suma total:", total)

print()
print("3.4.10 Intercambiar elementos")
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print("Lista invertida manualmente:", my_list)

print()
print("Invertir con for")
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("Lista invertida con for:", my_list)

print()
print("3.4.11 Beatles")
beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    new_member = input("Agrega un miembro de la banda: ")
    beatles.append(new_member)

print("Lista actual:", beatles)

del beatles[3]
del beatles[3]

beatles.insert(0, "Ringo Starr")
print("Lista final:", beatles)

print()
print("Quiz de seccion")

print()
print("Pregunta 1")
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

print()
print("Pregunta 2")
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

print()
print("Pregunta 4")
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))