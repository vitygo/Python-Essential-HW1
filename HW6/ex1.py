class MyIterator:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.index: int = 0

    def __iter__(self) -> 'MyIterator':
        return self  # Повертаємо сам обєкт як ітератор

    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # Генеруємо виключення, коли елементи закінчуються


my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)
