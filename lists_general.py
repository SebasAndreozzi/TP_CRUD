###IMPRIME LISTAS
def print_list(list:list, mensaje=""):

    for i in range(len(list)):
        print(f"{i+1}. {mensaje}{list[i]}")

###SUMA COLUMNAS
def column_addition(matrix:list, column:int) -> int|float:
    result = 0

    for i in range(len(matrix)):
        result += matrix[i][column]

    return result

###SUMA FILAS
def line_addition(matrix:list, line:int) -> int|float:
    result = 0

    for j in range(len(matrix[line])):
        result += matrix[line][j]

    return result