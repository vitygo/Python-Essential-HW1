from colorama import Fore, Style

class CarSalon:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
    
    def __str__(self) -> str:
        cars_string = '\n'.join([str(car) for car in self.cars])

        return (
            f"{Fore.RED}Автосалон {self.name}{Style.RESET_ALL}\n"
            f"{Fore.YELLOW}Машини автосалону:{Style.RESET_ALL}\n"
            f"{Fore.GREEN}{cars_string}{Style.RESET_ALL}"
        )

    def add_car(self, car:"Car"):
        print(f"Нова Машина в салоні {self.name} {car.model}, {car.year}року, Вартістю ${car.price}")
        self.cars.append(str(car))

    def sell_car(self):
        print(
            f"'1' {self.cars[0]}"
            f"'2' {self.cars[1]}"
        )
        user_choice = int(input("Оберіть Автомобіль: "))
        if user_choice == 1:
            print(f"{self.cars[0]} Продано!")
            del self.cars[0]
        elif user_choice == 2:
            print(f"{self.cars[1]} Продано!")
            del self.cars[1]
        avaliable_cars = '\n'.join([str(car) for car in self.cars])
        print(avaliable_cars)
        

        

class Car:
    def __init__(self, model:str, year:int, price:int):
        self.model = model
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return f"Машина: {self.model}\nРік: {self.year}\nЦіна: ${self.price}\n"
    
 
autoria = CarSalon("AUTO.RIA")
car1 = Car('BMW M3', 2019, 100000)
car2 = Car('Porshe Panamera', 2015, 90000)

autoria.add_car(car1)
autoria.add_car(car2)

autoria.sell_car()

print(autoria)
