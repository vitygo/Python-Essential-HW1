from ex2 import * 

# Перевірка наявності атрибутів
attributes = ['surname', 'name', 'age', 'mob_phone', 'email', 'job']

for attr in attributes:
    print(f"Has '{attr}' in contact_1:", hasattr(contact_1, attr))
    print(f"Has '{attr}' in update_contact_1:", hasattr(update_contact_1, attr))

# Отримання значень атрибутів
for attr in attributes:
    if hasattr(contact_1, attr):
        print(f"getattr(contact_1, '{attr}'): {getattr(contact_1, attr)}")
    if hasattr(update_contact_1, attr):
        print(f"getattr(update_contact_1, '{attr}'): {getattr(update_contact_1, attr)}")

# Встановлення нових значень атрибутів
setattr(contact_1, 'email', 'newemail@example.com')
setattr(update_contact_1, 'job', 'poet')

# Перевірка змінених значень
print("Updated contact_1 email:", contact_1.email)
print("Updated update_contact_1 job:", update_contact_1.job)

# Видалення атрибутів
delattr(contact_1, 'mob_phone')  # Видалимо атрибут, який існує
print(f"Has 'mob_phone' in contact_1 after deletion:", hasattr(contact_1, 'mob_phone'))

