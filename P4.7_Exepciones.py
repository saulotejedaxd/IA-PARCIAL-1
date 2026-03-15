print("4.7 Excepciones")

print()
print("4.7.1 Errores en el codigo")
print("Los programas pueden fallar por datos incorrectos o por errores del programador.")

print()
print("4.7.2 Cuando los datos no son lo que deberian ser")

try:
    value = int("25")
    print("Reciproco:", 1 / value)
except:
    print("Ocurrio un error")

print()
print("Ejemplo con ValueError")
try:
    value = int("hola")
    print(value)
except ValueError:
    print("Entrada incorrecta...")

print()
print("Ejemplo con ZeroDivisionError")
try:
    value = 0
    print(10 / value)
except ZeroDivisionError:
    print("No se puede dividir entre cero")

print()
print("4.7.3 try - except")
try:
    number = int("8")
    print(number / 2)
except:
    print("No se que hacer con eso")

print()
print("4.7.5 Manejar mas de una excepcion")
try:
    value = int("0")
    print(5 / value)
except ValueError:
    print("Valor incorrecto")
except ZeroDivisionError:
    print("Lo siento. No puedo dividir entre cero.")

print()
print("Excepcion por defecto")
try:
    value = int("abc")
    print(5 / value)
except ValueError:
    print("Valor incorrecto")
except ZeroDivisionError:
    print("No puedo dividir entre cero")
except:
    print("Algo salio mal")

print()
print("4.7.7 Algunas excepciones utiles")

print("ZeroDivisionError")
try:
    print(1 / 0)
except ZeroDivisionError:
    print("division by zero")

print()
print("TypeError")
try:
    short_list = [1]
    one_value = short_list[0.5]
    print(one_value)
except TypeError:
    print("indice invalido")

print()
print("AttributeError")
try:
    short_list = [1]
    short_list.append(2)
    short_list.depend(3)
except AttributeError:
    print("metodo inexistente")

print()
print("ValueError")
try:
    x = int("python")
    print(x)
except ValueError:
    print("no se pudo convertir a entero")

print()
print("4.7.11 Print debugging")
x = 5
print("Debug: x vale", x)

y = x * 2
print("Debug: y vale", y)

z = y - 3
print("Debug: z vale", z)

print()
print("4.7.14 Resumen practico")
while True:
    try:
        number = int(input("Ingresa un numero entero: "))
        print(number / 2)
        break
    except ValueError:
        print("Advertencia: el valor ingresado no es un numero valido. Intenta de nuevo...")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except:
        print("No se que hacer...")

print()
print("Prueba de seccion")

print()
print("Pregunta 1")
print("Si el usuario ingresa 0, la salida es:")
print("Entrada errónea...")

print()
print("Pregunta 2")
print("Si el usuario ingresa 0, ocurre TypeError")
print("porque value es cadena y no se puede hacer 10 / value")