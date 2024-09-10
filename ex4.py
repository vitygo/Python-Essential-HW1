from colorama import Fore, Style

class  CarDealership:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
    
    def __str__(self) -> str:
        return f"Салон: {self.name}\n"

    def add_car(self, car:"Car"):
        self.cars.append(car)
        

    def show_cars(self):
        if self.cars:
            print('Доступні авто: ')
            for num, car in enumerate(self.cars):
                print(f"({num+1}), {car}")
        else:
             print(f'Немає доступних автівок на {self.name}')

    def sell_car(self):
        print(f"{len(self.cars)} авто в доступі")
        self.show_cars()
        user_choice = int(input("Оберіть авто по номеру: "))
        sold =self.cars.pop(user_choice-1)
        print(f"{sold.make} {sold.model} продано")
        
        

class Car:
    def __init__(self, make:str, model:str, year:int, price:int):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return (f"Марка: {self.make}\n"
                f"Модель: {self.model}\n"
                f"Рік: {self.year}\n"
                f"Ціна: ${self.price}\n"
                )
    
autoria = CarDealership("AUTO.RIA")
car1 = Car('BMW', 'm3', 2019, 100000)
car2 = Car('Porshe', 'Panamera', 2015, 90000)
autoria.add_car(car1)
autoria.add_car(car2)
autoria.show_cars()
autoria.sell_car()

print(autoria)
