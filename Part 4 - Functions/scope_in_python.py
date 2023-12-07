a = 99
# def print_a_2():
#     a = 23
#     print(a)

# def print_a():
#     a = 2
#     print(a)

# print_a_2()

# def test_function(a):
#     a += 2
#     return a
# a = test_function(a)
# print(a)

print("====EXERCISE====")
multiplier = 100
has_calculated = False

def multiply_calculator(number):
    result = number * multiplier
    global has_calculated; has_calculated = True
    return result

print(multiply_calculator(9))
print(has_calculated)