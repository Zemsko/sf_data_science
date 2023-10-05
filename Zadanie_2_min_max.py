
DEFAULT_INPUT_SEPARATOR = ' '

def convert_str_to_float_list(input_string):
    result_float_list = []

    # if input string is empty
        
    if input_string == "":
        return result_float_list

    input_string = input_string.replace(",", ".")    
    input_str_list = input_string.split(DEFAULT_INPUT_SEPARATOR)
   
    for stringValue in input_str_list:
        try:
            result_float_list.append(float(stringValue))
        except ValueError:
            continue
    return result_float_list

    
def find_min_max(input_float_list):
    return min(input_float_list), max(input_float_list)


input_str = input('Введите последовательность: ')
input_list = convert_str_to_float_list(input_str)
if len(input_list) == 0:
    print("Введена пустая строка")
else:
    f_min, f_max = find_min_max(input_list)
    print("Minimum:", f_min)
    print("Maximum:", f_max)



