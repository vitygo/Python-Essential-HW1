from ex2 import *

# Створюємо два екземпляри кожного класу
contact_1 = Contact("Serhiy", "Zhadan", 50, 123456789, "Zhadan@gmail.com")
contact_2 = Contact("Oksana", "Zabuzhko", 63, 234567890, "Zabuzhko@gmail.com")

update_contact_1 = UpdateContact("Taras", "Shevchenko", 210, 987654321, "kobzar@gmail.com", "writer")
update_contact_2 = UpdateContact("Lesya", "Ukrainka", 150, 876543210, "ukrainka@gmail.com", "poetess")

def print_class_info(cls):
    print(f"Class {cls.__name__}:")
    print(f"Attributes: {cls.__dict__}")

def print_instance_info(instance):
    print(f"Instance of {instance.__class__.__name__}:")
    print(f"Attributes: {instance.__dict__}")

# Виведення інформації до видалення атрибуту
print_class_info(Contact)
print_class_info(UpdateContact)

print_instance_info(contact_1)
print_instance_info(contact_2)
print_instance_info(update_contact_1)
print_instance_info(update_contact_2)

# Видалення атрибуту 'job' з екземплярів класу UpdateContact
delattr(update_contact_1, 'job')
delattr(update_contact_2, 'job')

# Виведення інформації після видалення атрибуту
print("After deleting 'job' attribute:")
print_instance_info(update_contact_1)
print_instance_info(update_contact_2)

# Порівняння
print(f"UpdateContact instance 1 before removal: {update_contact_1.__dict__}")
print(f"UpdateContact instance 1 after removal: {update_contact_1.__dict__}")

print(f"UpdateContact instance 2 before removal: {update_contact_2.__dict__}")
print(f"UpdateContact instance 2 after removal: {update_contact_2.__dict__}")