def print_options(general):
       print('view_print_params', general * 2)

print_options('- double_sided')
print_options('- number_of_sheets')


import random
def print_settings():
    print_options = [' number_of_copies', ' double_sided_printing', ' print_quality', ' Color_print']
    basic_printer_settings = random.choice(print_options)
    return basic_printer_settings * 2

basic_printer_settings = print_settings()
print(basic_printer_settings)



def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = [value] * m
        matrix.append(row)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)