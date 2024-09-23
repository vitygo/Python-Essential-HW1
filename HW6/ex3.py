class ReverseIterator:
    def __init__(self, iterable:list):
        self.iterable = iterable
        self.index:int = len(iterable)  # Починаємо з довжини, щоб отримати останній елемент

    def __iter__(self) -> 'ReverseIterator':
        return self  # Повертаємо сам об'єкт як ітератор

    def __next__(self):
        if self.index > 0:  # Якщо індекс більший за 0
            self.index -= 1  # Зменшуємо індекс
            return self.iterable[self.index]  # Повертаємо елемент
        else:
            raise StopIteration  # Генеруємо виключення, коли елементи закінчуються


my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)

for item in reverse_iterator:
    print(item)