products = {
    "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
    "Одяг": ["Футболка", "Джинси", "Куртка"],
    "Книги": ["Роман", "Фентезі", "Наукова література"]
}


class StoreIter:
    def __init__(self, data):
        self.data = data
        self.category = data.keys()
    


    def __iter__(self) -> 'StoreIter':
        return self
    
    def __next__(self):
        
        for category in self.category:

            return self.data[category]
        
    
si = StoreIter(products)

for el in si:
    print(el)
