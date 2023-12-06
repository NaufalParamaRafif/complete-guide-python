# x = 0
# while x < 10:
#     x += 1
#     if x == 5:
#         continue
#     if x == 9:
#         break
#     print(x)
# print(x + 1)

print("====EXERCISE====")
even_number = []
# x = 1
# while x <= 100:
#     if x % 2 == 0:
#         even_number.append(x)
#     x += 1

# simple solution but not that worst
x = 0
while x < 100:
    x += 2
    if x == 58:
        continue
    even_number.append(x)
print(even_number)
    