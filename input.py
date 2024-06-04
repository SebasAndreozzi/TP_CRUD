from lists_general import print_list

def get_int(message:str, message_error:str, min:int, max:int) -> int:
    
    try:
        result = int(input(f"{message}"))

        while result < min or result > max:

            result = int(input(f"{message_error}"))
        
        return result
    except:
        return get_int(message_error, message_error, min, max)

def get_int_no_max(message:str, message_error:str, min:int) -> int:
    
    try:
        result = int(input(f"{message}"))

        while result < min:

            result = int(input(f"{message_error}"))
        
        return result
    except:
        return get_int(message, message_error, min)

def get_option(message:str, message_error:str, option_list:list) -> int:
    
    print_list(option_list)
    entry = get_int(message, message_error, 1, len(option_list))
    
    result = entry -1
    return result

def get_string(message:str, message_error:str, length:int) -> str:
    
    result = str(input(f"{message}"))

    while len(result)> length or len(result) < 1:

        result = str(input(f"{message_error}"))
        
    return result


def get_string_alpha(message:str, message_error:str, length:int) -> str:
    
    result = str(input(f"{message}"))

    while result.isalpha() == False or len(result) > length or len(result) < 1:

        result = str(input(f"{message_error}"))
        
    return result

def get_string_no_length(message:str) -> str:
    
    result = str(input(f"{message}"))
        
    return result

def get_dichotomy(message:str, message_error:str, option_true:str|int|float, option_false:str|int|float) -> bool:

    result = get_string_no_length(message, message_error)

    while result != option_true and result != option_false:
        result = get_string_no_length(message_error, message_error)
    
    return result