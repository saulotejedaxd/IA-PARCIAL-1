print("2.6 Interaccion con el usuario")

print()
print("La funcion input() permite recibir datos del usuario.")

print()
nombre = input("Escribe tu nombre: ")
print("Hola", nombre)

print()
print("Ejemplo simple con input")
anything = input("Dime algo: ")
print("Hmm...", anything, "... interesante")

print()
print("El resultado de input() es una cadena")
numero = input("Ingresa un numero: ")
print("El valor ingresado fue:", numero)

print()
print("Conversion de tipos")

numero = input("Ingresa un numero para elevarlo al cuadrado: ")
numero = int(numero)
print("El cuadrado es:", numero ** 2)

print()
print("Uso de float()")

num = float(input("Ingresa un numero decimal: "))
print("El numero multiplicado por 2 es:", num * 2)

print()
print("Concatenacion de cadenas con +")

nombre = input("Escribe tu nombre otra vez: ")
print("Bienvenido " + nombre)

print()
print("Replicacion de cadenas con *")

texto = input("Escribe una palabra: ")
print(texto * 3)

print()
print("LAB simple de operaciones")

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

print("Suma =", a + b)
print("Resta =", a - b)
print("Multiplicacion =", a * b)
print("Division =", a / b)

print()
print("Ejemplo de conversion a cadena con str()")

edad = 20
print("Tengo " + str(edad) + " anos")