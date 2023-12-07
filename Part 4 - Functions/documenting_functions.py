def add_two_variable(first_variable:int = 10, second_variable:int = 2) -> int:
    '''function that return the result from adding two variable'''
    return first_variable + second_variable

# print(add_two_variable('Naufal',' Parama')) # work too
print(add_two_variable(3,76))
print(add_two_variable.__doc__)
help(add_two_variable)