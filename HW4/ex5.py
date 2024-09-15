# Exception для випадку, коли тренера не знайдено
class TrainerNotFoundException(Exception):
    def __init__(self, last_name):
        self.last_name = last_name
        super().__init__(f"Тренера з прізвищем '{self.last_name}' не знайдено")

sports_info = [
    {
        'sport': 'Джіу-джітсу',
        'trainer': 'Мельник',
        'schedule': 'Понеділок, Середа, П\'ятниця - 18:00',
        'price': 250
    },
    {
        'sport': 'Боротьба',
        'trainer': 'Шевченко',
        'schedule': 'Вівторок, Четвер - 17:00',
        'price': 220
    },
    {
        'sport': 'Бокс',
        'trainer': 'Усик',
        'schedule': 'Середа, П\'ятниця - 16:00',
        'price': 180
    },
    {
        'sport': 'Тайський бокс',
        'trainer': 'Фюрі',
        'schedule': 'Понеділок, Четвер - 19:00',
        'price': 200
    }
]


def show_menu():
    print("Меню:")
    print("1 - Перелік видів спорту")
    print("2 - Команда тренерів")
    print("3 - Розклад тренувань")
    print("4 - Вартість тренувань")
    print("5 - Пошук тренера по прізвищу")
    print("6 - Вихід")

def show_sports():
    print("Перелік видів спорту:")
    for sport in sports_info:
        print(f"- {sport['sport']}")

def show_trainers():
    print("Команда тренерів:")
    for sport in sports_info:
        print(f"- Тренер {sport['trainer']} (вид спорту: {sport['sport']})")

def show_schedule():
    print("Розклад тренувань:")
    for sport in sports_info:
        print(f"- {sport['sport']}: {sport['schedule']}")


def show_prices():
    print("Вартість тренувань:")
    for sport in sports_info:
        print(f"- {sport['sport']}: {sport['price']} грн за одне тренування")

def search_trainer():
    last_name = input("Введіть прізвище тренера для пошуку: ")
    try:
        for sport in sports_info:
            if sport['trainer'] == last_name:
                print(f"Тренер {last_name} тренує {sport['sport']}. Розклад: {sport['schedule']}. Вартість: {sport['price']} грн.")
                return
        raise TrainerNotFoundException(last_name)
    except TrainerNotFoundException as e:
        print(e)


def main():
    while True:
        show_menu()
        choice = input("Виберіть пункт меню: ")
        
        if choice == '1':
            show_sports()
        elif choice == '2':
            show_trainers()
        elif choice == '3':
            show_schedule()
        elif choice == '4':
            show_prices()
        elif choice == '5':
            search_trainer()
        elif choice == '6':
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз!")

main()
