from ex2 import * 

# Створюємо два екземпляри кожного класу
contact_1 = Contact("Serhiy", "Zhadan", 50, 123456789, "Zhadan@gmail.com")
contact_2 = Contact("Oksana", "Bilozir", 45, 234567890, "Bilozir@gmail.com")

update_contact_1 = UpdateContact("Taras", "Shevchenko", 210, 987654321, "kobzar@gmail.com", "writer")
update_contact_2 = UpdateContact("Lesya", "Ukrainka", 150, 876543210, "ukrainka@gmail.com", "poetess")

# Перевірка типу екземплярів за допомогою isinstance()
print("Is contact_1 an instance of Contact?", isinstance(contact_1, Contact))  # True
print("Is contact_1 an instance of UpdateContact?", isinstance(contact_1, UpdateContact))  # False

print("Is update_contact_1 an instance of Contact?", isinstance(update_contact_1, Contact))  # True
print("Is update_contact_1 an instance of UpdateContact?", isinstance(update_contact_1, UpdateContact))  # True

# Перевірка спадкових відносин між класами за допомогою issubclass()
print("Is Contact a subclass of UpdateContact?", issubclass(Contact, UpdateContact))  # False
print("Is UpdateContact a subclass of Contact?", issubclass(UpdateContact, Contact))  # True