from ex2 import *

print("Methods of Contact:")
for method in dir(Contact):
    if callable(getattr(Contact, method)) and not method.startswith("__"): 
        print(method)

print("Methods of UpdateContact:")
for method in dir(UpdateContact):
    #callable(): Це вбудована функція Python, яка перевіряє, чи може об'єкт бути викликаний як функція або метод
    
    #getattr(Contact, method): Функція getattr отримує значення атрибута (в даному випадку — методу) 
    # з об'єкта або класу Contact. Тобто, getattr(Contact, method) поверне атрибут з ім'ям method з класу Contact.
    if callable(getattr(UpdateContact, method)) and not method.startswith("__"):
        print(method)
