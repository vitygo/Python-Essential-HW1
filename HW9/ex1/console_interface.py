import sys
from url_shortener import URLShortener

class ConsoleInterface:
    def __init__(self):
        self.shortener = URLShortener()

    def start(self):
        while True:
            print("\n1. Додати нове посилання")
            print("2. Отримати початкове посилання")
            print("3. Вийти")
            choice = input("Виберіть дію (1/2/3): ")

            if choice == '1':
                self.add_url()
            elif choice == '2':
                self.get_url()
            elif choice == '3':
                sys.exit("Вихід з програми.")
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def add_url(self):
        short_link = input("Введіть коротку назву посилання: ")
        full_link = input("Введіть початкове посилання: ")
        try:
            self.shortener.add_url(short_link, full_link)
            print(f"Посилання '{short_link}' успішно додано!")
        except ValueError as e:
            print(e)

    def get_url(self):
        short_link = input("Введіть коротку назву посилання для отримання: ")
        try:
            full_link = self.shortener.get_url(short_link)
            print(f"Повне посилання: {full_link}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    interface = ConsoleInterface()
    interface.start()