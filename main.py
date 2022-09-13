# Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.

def check_movements(matrix):
    x_count = 0
    o_count = 0
    for row in matrix:
        for el in row:
            if el == "X":
                x_count += 1
            elif el == "O":
                o_count += 1

    if (x_count+1) == o_count or x_count == (o_count+1):
        return True
    
    print("ERROR: Incorrect number of movements!")
    return False

def get_row(pos):
    if pos >= 1 and pos <= 3:
        return 0
    elif pos >= 4 and pos <= 6:
        return 1
    else:
        return 2

def get_col(pos):
    if pos == 1 or pos == 4 or pos == 7:
        return 0
    elif pos == 2 or pos == 5 or pos == 8:
        return 1
    else:
        return 2

def list_has_same_values(lst):
    return lst.count(lst[0]) == len(lst)

def matrix_checker(matrix):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], 
        [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]
    ]

    if check_movements(matrix):
        for con in win_conditions:
            values_to_check = []
            for el in con:
                values_to_check.append(matrix[get_row(el)][get_col(el)])
            
            if list_has_same_values(values_to_check):
                return values_to_check[0]

        return "Empate"
    else:
        return "Nulo"

print(matrix_checker(
        [
            ["O", "X", "X"],
            ["", "O", ""],
            ["O", "X", "O"]
        ]
    )
)

print(matrix_checker(
        [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["O", "X", "X"]
        ]
    )
)

print(matrix_checker(
        [
            ["X", "O", "O"],
            ["O", "O", "X"],
            ["X", "X", "O"]
        ]
    )
)

print(matrix_checker(
        [
            ["X", "X", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]
    )
)