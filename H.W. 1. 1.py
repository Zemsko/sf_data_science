input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')

list_1 = input_string1.split(', ')
list_2 = input_string2.split(', ')
try:
    def convert_str_int(list_1):
        for number in list_1:
            input_string1 = int(list_1)
        return input_string1
except ValueError:
    # Handle the exception
    print('Please enter an integer')
    
def pure_intersection(list_1, list_2):
    
    return (list_1.intersection(list_2))
result = list(set(pure_intersection(list_1, list_2)))
print('[{}]'.format(", ".join(result)))
