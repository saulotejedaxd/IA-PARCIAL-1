print("3.6 Operaciones con listas")

print()
print("3.6.1 Asignacion de listas")
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print("list_1 =", list_1)
print("list_2 =", list_2)

print()
print("3.6.2 Rebanadas")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print("Lista original:", my_list)
print("Rebanada [1:3]:", new_list)

print()
print("Copia completa con [:]")
copy_list = my_list[:]
print(copy_list)

print()
print("3.6.3 Rebanadas con indices negativos")
print(my_list[1:-1])
print(my_list[:3])
print(my_list[3:])
print(my_list[:])

print()
print("Eliminar rebanadas con del")
temp_list = [10, 8, 6, 4, 2]
del temp_list[1:3]
print(temp_list)

temp_list = [10, 8, 6, 4, 2]
del temp_list[:]
print(temp_list)

print()
print("3.6.4 Operadores in y not in")
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(8 in my_list)
print(8 not in my_list)

print()
print("3.6.5 Buscar el mayor")
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print("El mayor es:", largest)

print()
print("Buscar un elemento")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el indice", i)
else:
    print("ausente")

print()
print("Aciertos de loteria")
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print("Aciertos:", hits)

print()
print("3.6.6 Eliminar repetidos")
my_list = [1, 2, 3, 2, 4, 3, 5, 1]
new_list = []

for number in my_list:
    if number not in new_list:
        new_list.append(number)

print("Lista sin repetidos:", new_list)

print()
print("Quiz de seccion")

print()
print("Pregunta 1")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

print()
print("Pregunta 2")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

print()
print("Pregunta 3")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

print()
print("Pregunta 4")
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

print()
print("Pregunta 5")
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)
print("A" not in my_list)
print(3 not in my_list)
print(False in my_list)