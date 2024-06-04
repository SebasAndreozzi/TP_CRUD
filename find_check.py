def check_for_key_value(list:list[dict], key:str, value) -> bool:

    for  element in list:
        if element[key] == value:
            return True
    
    return False

def check_not_empty_list(list) -> bool:

    if len(list) > 0:
        return True
    
    return False

def find_by_key(employee_list:list[dict], key:str, value) -> int|None:

    element_position = None
    for i in range(len(employee_list)):
        if employee_list[i][key] == value:

            element_position = i
            break
    
    return element_position