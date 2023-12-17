class greetings:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return f"Hello {self.name}"
    
    def say_how_are_you(self):
        return f"Hey! How are you? {self.name}"
    
class goodbye:
    def __init__(self, name):
        self.name = name
    def say_goodbye(self):
        return f"Good bye {self.name}"
    def say_bye():
        return f"bye-bye..."

def sum(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

print(__name__)