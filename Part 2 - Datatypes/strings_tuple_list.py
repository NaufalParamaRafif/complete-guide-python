test_string = 'this is a test'
test_list = [1,2,3,4]

# convert a string into a list / tuple
# print(test_string.split())
# print(list(test_string))
# print(tuple(test_string))

# convert a list / tuple into string
# print(' '.join(['Naufal', 'Parama', 'Rafif']))
# print(type(str(test_list)))

# indexing on string
# print(test_string[::-1])

print("====EXERCISE====")
# solution = str(test_list)[1:-1:]
# print(' '.join(solution[::3]))
solution = (str(test_list)).strip('[').strip(']').replace(',', '')
print(solution)