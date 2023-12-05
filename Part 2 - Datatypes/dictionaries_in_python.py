# basics
my_dictionaries = {
    123321: "Anis",
    123322: "Avatar",
    123323: "Bayu"
}
# print(my_dictionaries.values())

# converting dictionaries
# print(list(my_dictionaries))

# indexing with dicttionaries
# print(my_dictionaries[123321])
# print(my_dictionaries.get(123321)) # better

print("====EXERCISE====")
# my_dictionaries[123324] = "Biska"
my_dictionaries.update({123324: "Biska"})
print(my_dictionaries)