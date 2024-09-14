class IncreasSalaryError(Exception):
    pass

class Employee:
    employees = []
    def __init__(self, name:str, age:int, position:str, start_year:int, salary:int):
        if not name.isalpha():
            raise ValueError("Ім'я повинно містити лише літери")
        if not position:
            raise ValueError("Вкажіть відділ")
        if not isinstance(start_year, int):
            raise ValueError("Рік повинен бути числом")
        
        self.name = name 
        self.age = age
        self.position = position
        self.start_year = start_year
        self.salary = salary
        Employee.employees.append(self)
        
    
    def __str__(self):
        return (f"Імя: {self.name}\n"
                f"Вік: {self.age}\n"
                f"Позиція: {self.position}\n"
                f"Початок роботи: {self.start_year}\n"
                f"Зарплата: ${self.salary}.\n"
                f"Зарплата в гривнях: UAH{self.usd_to_uah(self.salary)}")

    def increas_salary(self):
        print(self.salary)
        try:
            amount = int(input("на скільки збільшити зарплату?: "))
            if amount > 500:
                raise IncreasSalaryError("Ну це нагло аж так ми йому зарплату не піднімемо ")
        except ValueError:
            print("Веддіть число")
        else: # виконується якщо помилки не було
            self.salary += amount
            print(f"Нова зарплатня для {self.name}: {self.salary}")
        finally:
            print('Все відпрацвало') # виконується в любому випадку

    @classmethod
    def add_employees(cls):
        while True:
            try:
                name = input("Введіть ім'я: ")
                age = int(input("Введіть вік: "))
                position = input("Введіть посаду: ")
                start_year = int(input("Введіть рік початку роботи: "))
                salary = int(input("Введіть зарплату: "))
            
                employee = Employee(name, age, position, start_year, salary)
                
                cls.employees.append(employee)

                more = input("Чи бажаєте додати ще одного співробітника? (так/ні): ").strip().lower()
                if more != 'так':
                    break
            except Exception:
                print(f"Помилка, cпробуйте ще раз.")
        
    @classmethod
    def get_all_empoyes(cls):
        for employee in cls.employees:
            print(employee)
            print()

    @classmethod
    def get_all_new_empoyes(cls):
        actual_year = int(input("Введіть теперешній рік"))
        for employee in cls.employees:
            if employee.start_year == actual_year:
                print(employee)
                print()

    @staticmethod
    def usd_to_uah(amount:int) -> int:
        return amount * 41
        



employee1 = Employee("Viktor", 21, "python backend developer", 2025, 2000)
employee1.increas_salary()
print(employee1)

Employee.add_employees()
Employee.get_all_empoyes()
Employee.get_all_new_empoyes()
