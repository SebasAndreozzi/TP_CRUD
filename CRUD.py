from input import *
from find_check import *

MAX_EMPLOYEES = 20
MINIMUM_WAGE = 234315

message_name = "Nombre: "
message_name_error = "Nombre (Hasta 20 caracteres. Solo letras): "

message_surname = "Apellido: "
message_surname_error = "Apellido (Hasta 20 caracteres. Solo letras): "

message_dni = "DNI: "
message_dni_error = "DNI (Solo números sin '.' ní '-'): "

message_position = "Posisión: "
message_position_error = "Posición (Ingrese solo el número que corresponda a la posición): "
position_list = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]

message_salary = "Salario: "
message_salary_error = f"Salario (El salario mínimo es ${MINIMUM_WAGE}. Introdusca solo números): "

next_id = 1

############
###CREATE###
############

def create_employee(id:int, name:str, surname:str, dni:int, position:str, salary:float):

    employee = {
        "id" : id,
        "name" : name,
        "surname" : surname,
        "dni" : dni,
        "position" : position,
        "salary" : salary
        }
    
    return employee

def get_position(option_list:list) -> str:
    position = get_option(message_position, message_position_error, option_list)
    
    return option_list[position]

def load_employee(employee_list:list[dict]):
    global next_id

    id = next_id
    next_id += 1
    name = get_string_alpha(message_name, message_name_error, 20)
    surname = get_string_alpha(message_surname, message_surname_error, 20)
    dni = get_int(message_dni, message_dni_error, 5000000, 99999999)
    position = get_position(position_list)
    salary = get_int_no_max(message_salary, message_salary_error, MINIMUM_WAGE)

    employee = create_employee(id, name.capitalize(), surname.capitalize(), dni, position, salary)

    employee_list.append(employee)

############
####READ####
############

def show_employee(employee: dict):
    id = employee["id"]
    name = employee["name"]
    surname = employee["surname"]
    dni = employee["dni"]
    position = employee["position"]
    salary = employee["salary"]
    print(f"{id} -- {name} -- {surname} -- {dni} -- {position} -- {salary}")

def show_employee_list(employee_list:list[dict]):
    print("*" * 52)
    print(f"| {'Nombre':<10} | {'Apellido':<10} | {'Puesto':<10} | {'Salario':<10}|")
    print("-" * 52)
    
    for employee in employee_list:
        name = str(employee['name']).ljust(10)
        surname = str(employee['surname']).ljust(10)
        position = str(employee['position']).ljust(10)
        salary = str(employee['salary']).ljust(10)
        print(f"| {name} | {surname} | {position} | {salary}|")

    print("*" * 52)

############
###UPDATE###
############

def modify_employee(employee_list:list[dict]):
    entry = get_int_no_max("ID del empleado a modificar: ", "ID del empleado a modificar (Ingrese números enteros únicamente): ", 0)

    employee_list_position = find_by_key(employee_list, "id", entry)

    if employee_list_position != None:
        employee = employee_list[employee_list_position]

        while True:
            option_list = (list(employee)).remove("id")
            option_list.append("Salir")

            print_list(option_list)
            entry = get_int("¿Qué desea modificar?: ", "¿Qué desea modificar?(Las únicas opcioes son las que figuran en pantalla)", 1, len(option_list))

            match entry:
                case 1:
                    employee["name"] = get_string_alpha(message_name, message_name_error, 20)
                case 2:
                    employee["surname"] = get_string_alpha(message_surname, message_surname_error, 20)
                case 3:
                    employee["dni"] = get_int(message_dni, message_dni_error, 5000000, 99999999)
                case 4:
                    employee["position"] =  get_position(position_list)
                case 5:
                    employee["salary"] = get_int_no_max(message_salary, message_salary_error, MINIMUM_WAGE)
                case _:
                    show_employee(employee)
                    save = get_dichotomy("¿Desea guardar los cambios? si/no: ", "¿Desea guardar los cambios? si/no (las únicas opciones válidas son 'si' o 'no' en minusculas.): ", "si", "no")

                    if save:
                        employee_list[employee_list_position] = employee
                        print("Cambios guardados.")
                    else:
                        print("Cambios descartados.")
                    
                    break
    else:
        print("ID no encontrado")
                

############
###DELETE###
############

def delete_employee(employee_list:list[dict]):
    entry = get_int_no_max("ID del empleado a eliminar: ", "ID del empleado a eliminar (Ingrese números enteros únicamente): ", 0)

    employee_list_position = find_by_key(employee_list, "id", entry)
    
    if employee_list_position != None:
        employee_list.pop(employee_list_position)
    else:
        print("ID no encontrado")