import time

class Car:
    def __init__(self, make:str, model:str):
        self.make = make
        self.model = model
        self.key_turned_on = False
        self.__is_serpentine_belt = False # ремень генератора False значить що щось з ним не так

    def start_engine(self):
        self.key_turned_on = True
        if self.__is_serpentine_belt:
            if self.key_turned_on:
                print("You turned the key, which sends power from the battery to the ignition system and starter motor")
                time.sleep(1)
                self.__starter_motor_engages()
                time.sleep(1)
                self.__spray_fuel_into_the_engine()
                time.sleep(1)
                self.__spark_plug_ignites()
                time.sleep(1)
                self.__engine_start_running()
                time.sleep(1)
                self.__crankshaft_spin()
                time.sleep(1)
        else:
            print("Something wrong with serpantine belt, you cant start the engine")

    def __starter_motor_engages(self):
        print("The starter motor spins the engine a little bit to get it started")

    def __spray_fuel_into_the_engine(self):
        print("Fuel injectors spray fuel into the engine, and the air intake allows air to mix with the fuel")

    def __spark_plug_ignites(self):
        print("The spark plug creates a spark that ignites the fuel-air mixture in the engine's cylinders")

    def __engine_start_running(self):
        print("The ignition causes small explosions in the cylinders, which push pistons down, turning the crankshaft.")
    
    def __crankshaft_spin(self):
        print("The crankshaft keeps spinning, powering the rest of the engine and keeping it running.")
    
    def stop_engine(self):
        self.key_turned_on = False
        if not self.key_turned_on:
            time.sleep(1)
            print('engine stopped')
    # getter
    def get_serpentine_belt(self):
        return self.__is_serpentine_belt
    
    # setter
    def set_serpentine_belt(self):
        self.__is_serpentine_belt = True
        print("new serpentine belt is set")


        
car1 = Car("BMW", "M3")
car1.start_engine()
car1.set__serpentine_belt()
car1.start_engine()
