import pickle
import json


products = [
    {"id": 1, "name": "Laptop", "price": 15000, "quantity": 5},
    {"id": 2, "name": "Smartphone", "price": 8000, "quantity": 10},
    {"id": 3, "name": "Headphones", "price": 1500, "quantity": 50},
    {"id": 4, "name": "Keyboard", "price": 1200, "quantity": 30},
]

pickled_data = pickle.dumps(products)

with open('products.json', 'w') as json_file:
    json.dump({"pickled_products": pickled_data.hex()}, json_file)

print("Дані успішно збережено у файл 'products.json'")