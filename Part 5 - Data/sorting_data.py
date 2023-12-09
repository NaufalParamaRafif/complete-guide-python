# data = [1, 7, 2, 6, 4]
# # data.sort()
# complex_list = [['a', 2], ['b', 5], ['c', 9], ['d', 1], ['e', 6]]
# print(sorted(complex_list, key= lambda some_list: some_list[1], reverse= True))

inventory_name = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]
combined_list = list(zip(inventory_name, inventory_numbers))
print(sorted(combined_list, key=lambda list: list[1]))
print(sorted(combined_list, key=lambda list: len(list[0])))