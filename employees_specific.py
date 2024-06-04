from input import *
from listas_generales import print_list
from find_check import find_by_key

def get_average(values:list[int|float]) -> int|float:
    total = 0

    for value in values:
        total += value
    
    result = total / len(values)

    return result

def salary_average(employee_list:list[dict]) -> float:
    salary_list = []

    for employee in employee_list:
        salary_list.append(employee["salary"])
    
    result = get_average(salary_list)

    return result

def find_by_dni(employee_list:list[dict]) -> dict:
    entry = get_int("DNI: ", "DNI (Solo números sin '.' ní '-'): ", 5000000, 99999999)

    employee_position = find_by_key(employee_list, "dni", entry)

    if employee_position != None:
        return employee_list[employee_position]
    else:
        print("DNI no encontrado")

def min_to_max_value_int(employee_list:list[dict], key:str):
    for i in range(len(employee_list)):
        for j in range(0, len(employee_list)-i-1):
            if employee_list[j][key]  > employee_list[j+1][key]:
                auxiliar = employee_list[j]
                employee_list[j] = employee_list[j+1]
                employee_list[j+1] = auxiliar

def min_to_max_value_str(employee_list:list[dict], key:str):
    for i in range(len(employee_list)):
        for j in range(0, len(employee_list)-i-1):
            if employee_list[j][key][0]  > employee_list[j+1][key][0]:
                auxiliar = employee_list[j]
                employee_list[j] = employee_list[j+1]
                employee_list[j+1] = auxiliar

def max_to_min_value_int(employee_list:list[dict], key:str):
    for i in range(len(employee_list)):
        for j in range(0, len(employee_list)-i-1):
            if employee_list[j][key] < employee_list[j+1][key]:
                auxiliar = employee_list[j]
                employee_list[j] = employee_list[j+1]
                employee_list[j+1] = auxiliar

def max_to_min_value_str(employee_list:list[dict], key:str):
    for i in range(len(employee_list)):
        for j in range(0, len(employee_list)-i-1):
            if employee_list[j][key][0] < employee_list[j+1][key][0]:
                auxiliar = employee_list[j]
                employee_list[j] = employee_list[j+1]
                employee_list[j+1] = auxiliar


def sort_employee_list(employee_list:list[dict]):
    options = ["Nombre", "Apellido", "Salario"]
    ways = ["Ascendente", "Descendente"]

    print_list(options)
    entry_option = get_int("Ordenar por: ", "Ordenar por (Las únicas opciones disponibles son las que figuran en pantalla. Ingrese el número correspondiente): ", 1, len(options))
    print_list(ways)
    entry_way = get_int("En forma: ", "En forma (Las únicas opciones disponibles son las que figuran en pantalla. Ingrese el número correspondiente): ", 1, len(options))

    option = options[entry_option-1]
    way = ways[entry_way-1]

    if way == "Ascendente":
        match option:
            case "Nombre":
                min_to_max_value_str(employee_list, "name")
            case "Apellido":
                min_to_max_value_str(employee_list, "surname")
            case "Salario":
                min_to_max_value_int(employee_list, "salary")

    else:
        match option:
            case "Nombre":
                max_to_min_value_str(employee_list, "name")
            case "Apellido":
                max_to_min_value_str(employee_list, "surname")
            case "Salario":
                max_to_min_value_int(employee_list, "salary")