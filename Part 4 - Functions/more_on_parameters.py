# list unpacking
# def print_all_arguments(first, *all_arguments, extra):
#     print(first)
#     for argument in all_arguments:
#         print(argument)
#     print(extra)
# def calculator_and_name(*args, **kwargs):
#     result = 0
#     match kwargs['operator']:
#         case 'sum':
#             for number in args:
#                 result += number
#             print(result)
#         case 'product':
#             result = 1
#             for number in args:
#                 result *= number
#             print(result)
#     print(f"{kwargs['first_name']} {kwargs['middle_name']} {kwargs['last_name']}")


# # print_all_arguments('Namaku', 'Naufal', 'Parama', 'Rafif', extra='ya, benar')
# calculator_and_name(
#     1,2,3,4,5,6,7,8,9,10,
#     operator='sum',
#     first_name='Naufal',
#     middle_name='Parama',
#     last_name='Rafif'
# )

print("====EXERCISE====")

# def sum_all_number(*args):
#     total = 0
#     for number in args:
#         total += number
#     print(total)
# simple solution
def sum_all_number(*args):
    print(sum(args))

sum_all_number(12,12,12,12,12)