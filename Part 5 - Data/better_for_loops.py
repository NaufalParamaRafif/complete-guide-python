books = ["How to Read a Book", "Filosofi Teras", "Atomic Habits"]
book_authors = ["Mortimer J. Adler & Charles van Doren", "Henry Manampiring", "James Clear"]

# zip method
# for book, book_author in zip(books, book_authors):
#     print(f'the writer of {book} is {book_author}')

# enumerate
# for index, book in enumerate(books):
#     print(f'buku ke {index} adalah {book}')
#     if index == len(books) // 2:
#         print('Selesai setengah')

print('====EXERCISE====')
for index, book_and_book_author in enumerate(zip(books, book_authors)):
    print(f'{book_and_book_author[0]} [id: {index}] - Author: {book_and_book_author[1]}')