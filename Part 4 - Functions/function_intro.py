# def test_function():
#     print('hello')
#     test = 1 + 2
#     print(test)

# def calculator(num1, num2):
#     result = num1 + num2
#     print(result)

# calculator(32, 34)

print("====EXERCISE====")

def better_calculator(num1, num2, operator):
    match operator:
        case 'plus': result = num1 + num2; print(result)
        case 'minus': result = num1 - num2; print(result)

better_calculator(5, 3, 'minus')