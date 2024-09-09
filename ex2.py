class Book:
    def __init__(self, title:str, author:str, year:int, genre:str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.reviews = []

    def __str__(self) -> str:
        return (f"Title: {self.title} \n"
                f"Author: {self.author}\n" 
                f"Year: {self.year} \n"
                f"Genre: {self.genre} \n"
                f"\nВідгуки:"
                )

    def add_review(self, review):
        self.reviews.append(review)

    def show_reviews(self): #новий метод виводу review
        if self.reviews:
            for review in self.reviews:
                print(review)
        else:
             print(f'NO AVALIABLE REVIEWES FOR "{self.title}" BOOK!')

class Review: #добавив класс для Review
    def __init__(self, user_review:str, user_name:str = "Unknown user"):
        self.user_name = user_name
        self.user_review = user_review
    
    def __str__(self) -> str:
        return f"{self.user_name}: {self.user_review}"
    


book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
book2 = Book("1984", "George Orwell", 1949, "Dystopian")

review1 = Review(user_name='Мішаня', user_review='Чьотінька книжка, респект автору і уважуха')
review2 = Review(user_name='Kitty23', user_review='Лайк люблю толкіена')
review3 = Review(user_name='Дарт Вейдер',user_review='haha good good very good')
review4 = Review(user_name='Анатолій',user_review='продам гараж')
review5 = Review(user_review='Класно!')

book1.add_review(review1)
book1.add_review(review2)
book1.add_review(review3)
book1.add_review(review4)
book1.add_review(review5)



print(book1)
book1.show_reviews()
