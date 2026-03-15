from random import randrange


def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + str(row[0]) + "   |   " + str(row[1]) + "   |   " + str(row[2]) + "   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento: "))
            if move < 1 or move > 9:
                print("Número inválido. Debe estar entre 1 y 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] in ['X', 'O']:
                print("Ese cuadro ya está ocupado. Intenta de nuevo.")
                continue

            board[row][col] = 'O'
            break

        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free


def victory_for(board, sign):
    # Revisar filas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    # Revisar columnas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    # Revisar diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def draw_move(board):
    free = make_list_of_free_fields(board)
    if len(free) > 0:
        pos = randrange(len(free))
        row, col = free[pos]
        board[row][col] = 'X'


board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]

while True:
    display_board(board)

    if victory_for(board, 'X'):
        print("¡La máquina ha ganado!")
        break

    if victory_for(board, 'O'):
        print("¡Has Ganado!")
        break

    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        print("¡Empate!")
        break

    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("¡Has Ganado!")
        break

    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        print("¡Empate!")
        break

    draw_move(board)

    if victory_for(board, 'X'):
        display_board(board)
        print("¡La máquina ha ganado!")
        break

    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        display_board(board)
        print("¡Empate!")
        break