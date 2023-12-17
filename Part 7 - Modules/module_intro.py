import random, string
from random import * # we dont need to write random again
from math import floor as lower_value # just import library from math module, then named that function as lower_value function
# test = random.randint(0,2)
# print(test)

# test_list = []
# for i in range(10):
#     test_list.append(i + 1)
# print(random.choice(test_list))

print(string.ascii_letters)
print(lower_value(123.9))

print("====EXERCISE====")
from datetime import datetime
print(datetime.now())