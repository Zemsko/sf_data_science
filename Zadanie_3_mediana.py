import sys
DEFAULT_INPUT_SEPARATOR = ','


def convert_str_to_float_list(input_string):
    result_float_list = []
    # if input list is empty
    if input_string == "":
        return result_float_list
    # do string split using default separator
    input_str_list = input_string.split(DEFAULT_INPUT_SEPARATOR)
    try:
        for stringValue in input_str_list:
            result_float_list.append(float(stringValue))
        return result_float_list
    except ValueError:
        return None
    
    return result_float_list
    

def find_median(float_list):
    #get list length
    list_len = len(float_list)   

    # for empty list we can't calculate median
    if(list_len == 0):
        return None 

    if (list_len == 1): 
        return float_list[0]  

    # sort the list
    float_list.sort()

    # do floor devision to get median position
    half_len = list_len // 2

   # do modulo devision to get division remainder
    half_len_remainder = list_len % 2

   # if something in remainder that it's even set and we are at the mid point of it
    if (half_len_remainder > 0):
        return float_list[half_len]

   # nothing in the remainder, do left and right midpoint average
    else:
        left_number = float_list[half_len - 1]
        right_number = float_list[half_len]
        return (left_number + right_number) / 2

#ask user to enter some numbers
input_str = input('Введите последовательность:')
float_list = convert_str_to_float_list(input_str)

if(float_list == None):
    print('Некорректный ввод')
    sys.exit('Программа завершена с ошибкой')
    
median = find_median(float_list)
print("Median:", median)


            
