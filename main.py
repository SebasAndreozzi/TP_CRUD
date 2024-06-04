from input import *
from CRUD import *
from find_check import *
from employees_specific import *
from lists_general import print_list

messages_menu_1 = ["Ingresar empleado", "Modificar empleado", "Eliminar empleado", "Mostrar todos", "Calcular salario promedio","Buscar empleado por DNI", "Ordenar empleados", "Salir"]
messages_menu_1_entry = "Elija una opción: "
messages_menu_1_entry_error = "Elija una opción (Las únicas opciones disponibles son las que están en pantalla. Ingrese únicamente el número correspondiente): "

message_empty_list = "No hay ningún empleado cargado en sistema"

message_exit = "Hasta luego, que tengas muy buenos días te desea el equipo de Recursos Inhumanos."

list_employees = []

while True:
    print_list(messages_menu_1)
    menu_1_entry = get_int(messages_menu_1_entry, messages_menu_1_entry_error, 1, len(messages_menu_1))

    match menu_1_entry:
        
        case 1:
            if len(list_employees) <= 20:
                load_employee(list_employees)
            else:
                print("No hay más vacantes para empleados nuevos.")

        case 2:
            if check_not_empty_list(list_employees):
                modify_employee(list_employees)
            
            else:
                print(message_empty_list)
                 
        case 3:
            
            if check_not_empty_list(list_employees):               
                delete_employee(list_employees)
            
            else:
                print(message_empty_list)

        case 4:
            if check_not_empty_list(list_employees):
                show_employee_list(list_employees)
            
            else:
                print(message_empty_list)

        case 5:
            if check_not_empty_list(list_employees):
                salary_average(list_employees)
            
            else:
                print(message_empty_list)

        case 6:
            if check_not_empty_list(list_employees):
                empployee = find_by_dni(list_employees)
                show_employee(empployee)
            else:
                print(message_empty_list)

        case 7:
            if check_not_empty_list(list_employees):
                sort_employee_list(list_employees)
            
            else:
                print(message_empty_list)
        case 8:
            print(message_exit)
            break






