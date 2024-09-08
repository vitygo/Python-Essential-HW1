class Book:
    def __init__(self, title:str, author:str, year:int, genre:str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self) -> str:
        return f'Book(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}")'
    
    def __str__(self) -> str:
        return f" Title: {self.title} Author: {self.author} Year: {self.year} Genre: {self.genre}"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
book2 = Book("1984", "George Orwell", 1949, "Dystopian")
book3 = Book("Pride and Prejudice", "Jane Austen", 1813, "Romance")
book4 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Drama")
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")


print(repr(book1))
print(repr(book2))
print(repr(book3))
print(repr(book4))
print(repr(book5))

print(str(book1))
print(str(book2))
print(str(book3))
print(str(book4))
print(str(book5))