# number_100 = [(number, number+1, number+3) for number in range(1, 101)]
# print(number_100)

# even_number = [number for number in range(0, 101) if number % 2 == 0]
# print(even_number)
# even_number_change_odd_to_something = [number if number % 2 == 0 else f'{number} is not an even number' for number in range(0, 101)]
# print(even_number_change_odd_to_something)

# books = ["How to Read a Book", "Filosofi Teras", "Atomic Habits"]
# price_books = [120000, 90000, 80000]
# books_under_hundred = [(book, price_book) for book, price_book in zip(books, price_books) if price_book < 100000]
# print(books_under_hundred)

# combined_list_comperhension = [[(x, i) for x in range(5, 0, -1)] for i in range(1, 11)]
# for row in combined_list_comperhension:
#     print(row)

print("====EXERCISE====")
column_chess = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# chess_board_field = [[(f'{column}{row}') for column in column_chess] for row in range(1, 9)]
chess_board_field = [[(f'{column}{row}') for column in column_chess] for row in range(8, 0, -1)]
for row in chess_board_field:
    print(row)