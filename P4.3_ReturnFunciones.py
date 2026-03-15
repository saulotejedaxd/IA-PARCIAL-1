print("4.3 Devolviendo el resultado de una funcion")

print()
print("4.3.1 return sin expresion")

def happy_new_year(wishes=True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    print("¡Feliz año nuevo!")

happy_new_year()
print()
happy_new_year(False)

print()
print("return con expresion")

def boring_function():
    return 123

x = boring_function()
print("La funcion boring_function devolvio:", x)

print()
print("Ignorando el resultado de una funcion")

def boring_mode():
    print("'Modo aburrimiento' ON.")
    return 123

print("Esta leccion es interesante!")
boring_mode()
print("Esta leccion es aburrida...")

print()
print("4.3.2 None")

value = None
if value is None:
    print("Lo siento, no contienes ningun valor")

def strange_function(n):
    if n % 2 == 0:
        return True

print(strange_function(2))
print(strange_function(1))

print()
print("4.3.3 Listas y funciones")

def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

print(list_sum([5, 4, 3]))

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

print()
print("4.3.4 Año bisiesto")

def is_year_leap(year):
    if year < 1582:
        return False
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

print(2000, is_year_leap(2000))
print(2015, is_year_leap(2015))
print(1996, is_year_leap(1996))
print(1580, is_year_leap(1580))

print()
print("4.3.5 Cuantos dias")

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return days[month - 1]

print(days_in_month(2024, 2))
print(days_in_month(2023, 2))
print(days_in_month(2023, 13))

print()
print("4.3.6 Dia del año")

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None

    total = 0
    for m in range(1, month):
        total += days_in_month(year, m)
    return total + day

print(day_of_year(2024, 1, 1))
print(day_of_year(2024, 2, 29))
print(day_of_year(2023, 12, 31))

print()
print("4.3.7 Numeros primos")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")
print()

print()
print("4.3.8 Conversion de combustible")

def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100000 / 1609.344
    gallons = liters / 3.785411784
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1.609344
    liters_per_100km = 100 / (km_per_gallon / 3.785411784)
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

print()
print("Prueba de seccion")

print()
print("Pregunta 1")
def hi():
    return
    print("¡Hola!")

print(hi())

print()
print("Pregunta 2")
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

print()
print("Pregunta 3")
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))

print()
print("Pregunta 4")
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))