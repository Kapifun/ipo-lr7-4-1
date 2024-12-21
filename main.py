books = {
    1: {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    2: {"title": "Преступление и наказание", "author": "Федор Достоевский", "year": 1866},
    3: {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
    4: {"title": "Анна Каренина", "author": "Лев Толстой", "year": 1877},
    5: {"title": "Метро 2033", "author": "Дмитрий Глуховский", "year":2002}
}
#добавление новых книг
book_add = len(books) + 1

#цикл while
while True:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания книги: "))
    
    books[book_add] = {"title": title, "author": author, "year": year}
    book_add += 1
    
    cont = input("Хотите ли вы продолжить добавлять книги? (Y/N): ").lower()
    if cont != 'y':
        break

#цикл for
for book_add, book_info in books.items():
    print(f"---------------------- Книга {book_add} -----------------------")
    print(f"Название: {book_info['title']}, Автор: {book_info['author']},")
    print(f"-------------------------{book_info['year']}-------------------------")