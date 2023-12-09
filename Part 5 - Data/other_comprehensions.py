# set_comprehension = {num for num in range(1, 101)}
# print(set_comprehension)

# dictionary_comprehension = {num: (num * 10 % 2) for num in range(1, 51)}
# dictionary_comprehension = {num: (num * 2) for num in range(1, 51)}
# for index in dictionary_comprehension:    
#     print(dictionary_comprehension.items())
# for key, value in zip(dictionary_comprehension.keys(), dictionary_comprehension.values()):
#     print(f'{key}: {value}')

# tuple_comp = tuple(number for number in range(1, 101))
# print(tuple_comp)

print("====EXERCISE====")
solution_key = ['A', 'B', 'C', 'D', 'F']
# solution = {solution_key[i]: i+1 for i in range(0, 5)} # salah baca perintah XD
solution = {letter: [1, 2, 3, 4, 5] for letter in 'ABCDE'}
print(solution)