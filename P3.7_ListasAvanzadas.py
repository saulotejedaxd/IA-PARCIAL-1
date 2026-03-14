print("3.7 Aplicaciones avanzadas de listas")

print()
print("3.7.1 Comprension de listas")

row = ["PEON_BLANCO" for i in range(8)]
print("Fila de peones:", row)

squares = [x ** 2 for x in range(10)]
print("Cuadrados:", squares)

twos = [2 ** i for i in range(8)]
print("Potencias de 2:", twos)

odds = [x for x in squares if x % 2 != 0]
print("Impares de squares:", odds)

print()
print("3.7.2 Arreglo de dos dimensiones")

EMPTY = "VACIO"
board = [[EMPTY for i in range(8)] for j in range(8)]

print("Tablero vacio:")
print(board)

ROOK = "TORRE"
KNIGHT = "CABALLO"
PAWN = "PEON"

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[4][2] = KNIGHT
board[3][4] = PAWN

print("Tablero con piezas:")
for row in board:
    print(row)

print()
print("Acceso a posiciones especificas")
print("board[0][0] =", board[0][0])
print("board[4][2] =", board[4][2])
print("board[3][4] =", board[3][4])

print()
print("3.7.3 Ejemplo estacion meteorologica")

temps = [[0.0 for h in range(24)] for d in range(31)]

temps[0][11] = 22.5
temps[1][11] = 24.0
temps[2][11] = 19.5
temps[3][11] = 21.0

total = 0.0
for day in temps:
    total += day[11]

average = total / 31
print("Temperatura promedio al mediodia:", average)

highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura mas alta fue:", highest)

hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print("Dias calurosos:", hot_days)

print()
print("Arreglo tridimensional")
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True
rooms[0][4][1] = False

vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("Habitaciones disponibles en el piso 15 del edificio 3:", vacancy)

print()
print("Resumen rapido")
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])
print(table[0][3])

print()
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])
print(cube[2][2][0])