# Створюємо базовий клас Contact
class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"Contact: {self.name} {self.surname}, Age: {self.age}, Phone: {self.mob_phone}, Email: {self.email}"

    def sent_message(self, message: str):
        return f"Sending message: '{message}' to {self.name} at {self.mob_phone}"


class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str, job: str):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"Contact {self.name} {self.surname} works as {self.job}"


contact_1 = Contact("Serhiy", "Zhadan ", 50, 123456789, "Zhadan@gmail.com")

update_contact_1 = UpdateContact("Taras", "Shevchenko", 210, 987654321, "kobzar@gmail.com", "writer")

print(contact_1.get_contact())  
print(contact_1.sent_message("І на оновленій землі врага не буде, супостата, а буде син і буде мати, і будуть люде на землі.")) 

print(update_contact_1.get_contact())  
print(update_contact_1.get_message())  


print(contact_1.__dict__)  
print(update_contact_1.__dict__)  

print(UpdateContact.__base__)  
print(UpdateContact.__bases__) 
