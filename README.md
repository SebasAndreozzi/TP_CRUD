# TP CRUD: Recursos Inhumanos

## Enunciado:

La empresa "Recursos Inhumanos" nos ha solicitado desarrollar un software de gestión de empleados para llevar a cabo un control exhaustivo de los mismos.

Datos correspondientes a cada empleado:
ID
Nombre
Apellido
DNI
Puesto
Salario

## Consideraciones:

El programa deberá gestionar una lista de hasta 20 empleados. Cada empleado será representado mediante un diccionario.

Si se alcanza el límite de 20 empleados, se deberá notificar al usuario. Solo se podrá ingresar un empleado en caso de que se efectúe una vacante nueva (o sea que se elimine uno).

Al ingresar un empleado, el ID debe ser autoincremental, comenzando en 1. Cada empleado tendrá un ID único.

El resto de los datos deberán ser ingresados por consola.

## Validaciones:

Nombre y Apellido: Deben contener solo caracteres alfabéticos, ser nombres propios y no exceder los 20 caracteres. No pueden contener números ni caracteres especiales.

Salario: Debe ser un valor numérico entero no menor a $234315.

Puesto: Debe ser uno de los siguientes: “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”.

DNI: Debe ser un valor numérico entre 5000000 y 99999999.

## Opciones del menú:

Ingresar empleado: Pedirá los datos necesarios y dará de alta a un nuevo empleado, asignando un ID autoincremental.

Modificar empleado: Permitirá alterar cualquier dato del empleado excepto su ID. Se usará el ID para identificar al empleado a modificar. Se mostrará un submenú para seleccionar qué datos modificar. Indicando si se realizaron modificaciones o no.

Eliminar empleado: Eliminará permanentemente a un empleado de la lista original. Se pedirá el ID del empleado a eliminar. 

Mostrar todos: Imprimirá por consola la información de todos los empleados en formato de tabla:

![Formato_de_lista](./img/employee_list_format.png)

Calcular salario promedio: Calculará e imprimirá el salario promedio de todos los empleados.

Buscar empleado por DNI: Permitir al usuario buscar y mostrar la información de un empleado específico ingresando su DNI.

Ordenar empleados: Ofrecer la opción de ordenar y mostrar la lista de empleados por nombre, apellido, o salario de forma ascendente o descendente.

Salir: Terminará la ejecución del programa.

## Requisitos adicionales:

El programa deberá estar correctamente modularizado, haciendo uso de módulos, paquetes y funciones propias para solicitar enteros, flotantes y cadenas, así como para las validaciones de cada uno de estos tipos de datos.
El código debe estar programado de manera eficiente y siguiendo buenas prácticas de la programación y las reglas de estilo de la cátedra.
