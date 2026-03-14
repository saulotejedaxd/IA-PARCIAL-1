print("3.3 Operadores logicos y operaciones bit a bit")

print()
print("3.3.1 Operadores logicos")

print("and")
print(True and True)
print(True and False)

print()
print("or")
print(True or False)
print(False or False)

print()
print("not")
print(not True)
print(not False)

print()
print("Expresiones logicas")
var = 1
print(var > 0)
print(not (var <= 0))

print(var != 0)
print(not (var == 0))

print()
print("Valores logicos con variables")
i = 1
j = not not i
print(j)

print()
print("3.3.4 Operadores bit a bit")
x = 15
y = 22

print("x =", x)
print("y =", y)

print()
print("Bit a bit and &")
print(x & y)

print()
print("Bit a bit or |")
print(x | y)

print()
print("Bit a bit xor ^")
print(x ^ y)

print()
print("Bit a bit not ~")
print(~x)

print()
print("Operaciones logicas vs bit a bit")
log = x and y
bit = x & y

print("Resultado logico:", log)
print("Resultado bit a bit:", bit)

print()
print("3.3.5 Manejo de bits con mascara")
flag_register = 0x1234
the_mask = 8

print("flag_register =", flag_register)
print("the_mask =", the_mask)

print()
print("Comprobar bit")
print(flag_register & the_mask)

print()
print("Resetear bit")
flag_register = flag_register & ~the_mask
print(flag_register)

print()
print("Establecer bit")
flag_register = flag_register | the_mask
print(flag_register)

print()
print("Negar bit")
flag_register = flag_register ^ the_mask
print(flag_register)

print()
print("3.3.6 Desplazamientos")
value = 17

print("value =", value)
print("value >> 1 =")
print(value >> 1)

print("value << 2 =")
print(value << 2)

print()
print("Mas ejemplos de desplazamiento")
print(8 >> 1)
print(8 >> 2)
print(3 << 1)
print(3 << 2)

print()
print("Quiz de seccion")

print()
print("Pregunta 1")
x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not(z))

print()
print("Pregunta 2")
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)