def add(a,b):
    return a + b
class Test:
    def __init__(self, some_function):
        self.first_function = some_function

test = Test(add)
print(test.first_function(21,21))