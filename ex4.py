from colorama import Fore, Style

class CarSalon:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
    
    def __str__(self) -> str:
        ...

    def add_car(self, car:"Car"):
        ...

    def sell_car(self):
        ...
        


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
