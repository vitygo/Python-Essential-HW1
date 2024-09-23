class Library:
    def __init__(self, name="CENTRAL LIBRARY"):
        self.name: str = name
        self.authors: list = []
        self.library_info: int = self.info()
        self._current_author = 0  # Для ітерації по авторам

    def info(self):
        print(f"У бібліотеці {len(self.authors)} авторів "
              f"та загалом {self.books_cnt()} книг.")

    def books_cnt(self) -> int:  # Підрахунок книг в бібліотеці
        cnt = 0
        for author in self.authors:
            cnt += len(author.books)
        return cnt

    def add_author(self, author: "Author"):
        self.authors.append(author)

    def __iter__(self):  
        self._current_author = 0
        return self
    
    def __next__(self):
        if self._current_author < len(self.authors):
            current = self.authors[self._current_author]
            self._current_author += 1
            return current
        else:
            raise StopIteration


class Author:
    def __init__(self, name: str):
        self.name = name
        self.books: list = []
        self._current_book = 0  # Для ітерації по книгах

    def __str__(self) -> str:
        return f"Автор: {self.name}"

    def show_books(self):
        for book in self.books:
            print(book, end="\n\n")

    def __iter__(self):  # Ітератор для книг автора
        self._current_book = 0
        return self

    def __next__(self):
        if self._current_book < len(self.books):
            current_book = self.books[self._current_book]
            self._current_book += 1
            return current_book
        else:
            raise StopIteration  


class Book:
    def __init__(self, author: "Author", title: str, year: int, genre: str):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.author.books.append(self)  # При створенні книги додається до автора

    def __str__(self):
        return (f"Книга: '{self.title}' \n"
                f"Автор: {self.author} \n"
                f"Жанр: {self.genre} \n"
                f"Рік видання: {self.year}")


# Створюємо бібліотеку
library = Library()

# Додаємо авторів
author1 = Author("J.K. Rowling")
author2 = Author("George Orwell")
author3 = Author("Agatha Christie")

# Додаємо авторів до бібліотеки
library.add_author(author1)
library.add_author(author2)
library.add_author(author3)

# Додаємо книги автору1
book1 = Book(author1, "Harry Potter", 1997, "Фантастика")
book2 = Book(author1, "The Running Grave", 2023, "Кримінал")

# Додаємо книги автору2
book3 = Book(author2, "1984", 1949, "Антиутопія")
book4 = Book(author2, "Animal Farm", 1945, "Сатира")

# Додаємо книги автору3
book5 = Book(author3, "Murder on the Orient Express", 1934, "Детектив")
book6 = Book(author3, "And Then There Were None", 1939, "Детектив")

# Виводимо книги авторів
author1.show_books()
author2.show_books()
author3.show_books()

# Виводимо інформацію про бібліотеку
library.info()

# Перебір всіх авторів у бібліотеці через ітератор
for author in library:
    print(author)
