import sys
import json

def main():
    while True:
        print("\n1. Додати нове посилання")
        print("2. Отримати початкове посилання")
        print("3. Вийти")
        choice = input("Виберіть дію (1/2/3): ")

        if choice == '1':
            add_url()
        elif choice == '2':
            get_url()
        elif choice == '3':
            sys.exit("Вихід з програми.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def add_url():
    with open("link.json", "r") as file:
        link_data = json.load(file)

    user_link = {"short_link": input("Введіть коротку назву посилання: ").lower().strip(),
                  "full_link": input("Введіть початкове посилання: ").strip().lower()}
    
    link_data.append(user_link)

    with open("link.json", "w") as file:
        json.dump(link_data, file, indent=4)


def get_url():
    short_name = input("Введіть коротку назву посилання для отримання: ").strip().lower()
    
    with open('link.json', 'r') as file:
        link_data = json.load(file)
        
        for link in link_data:
            if link["short_link"] == short_name:
                print(link['full_link'])


if __name__ == "__main__":
    main()

