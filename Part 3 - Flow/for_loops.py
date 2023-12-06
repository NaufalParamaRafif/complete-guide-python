# barang_elektronik = ["laptop", "keyboard", "mouse"]
# for setiap_barang in barang_elektronik:
#     print(f'{setiap_barang} masih bekerja dengan baik')
for x in range(100, 0, -1):
    print(x)

print("====EXERCISE====")
practice_list = [[10,40,20,50], [2, 42, 10], [101, 10, 4]]

for each_container in practice_list:
    for each_value in each_container:
        if each_value < 10:
            continue
        elif each_value < 50:
            print(each_value)
        elif each_value > 100:
            break