# map - change value one by one
my_list = [1, 2, 3, 4, 5]
# change_my_list_one_by_one = map(lambda one_item: one_item * 10 ** 2, my_list)
# print(list(change_my_list_one_by_one))

# filter get some value through some condition
# filtered_my_list = filter(lambda one_item: one_item > 2, my_list) # jika mau return something tapi gak mau else
# print(list(filtered_my_list))

print("====EXERCISE====")
mapped_list_comprehension = [value ** 2 for value in my_list]
filtred_list_comprehension = [value for value in my_list if value < 4]
print(mapped_list_comprehension)
print(filtred_list_comprehension)