from colorama import Fore, Style

class Book:
    def __init__(self, title:str, author:str, year:int, genre:str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.reviews = []

    def __str__(self) -> str:
        reviews_string = '\n'.join(self.reviews)
        return (f"Title: {self.title} \n"
                f"Author: {self.author}\n" 
                f"Year: {self.year} \n"
                f"Genre: {self.genre} \n\n"
                f"Reviews:\n{reviews_string}")

    def add_review(self, review:str, user_name:str='Unknown User'):
        self.reviews.append(f"{Fore.RED}Користувач{Style.RESET_ALL} {Fore.YELLOW}{user_name}{Style.RESET_ALL}: {review}")


book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
book2 = Book("1984", "George Orwell", 1949, "Dystopian")


book1.add_review(user_name='Мішаня', review='Чьотінька книжка, респект автору і уважуха')
book1.add_review(user_name='Kitty23', review='Лайк люблю толкіена')
book1.add_review(user_name='Дарт Вейдер', review='haha good good very good')
book1.add_review(user_name='Анатолій', review='продам гараж')
book1.add_review(review='Класно!')



print(book1)
