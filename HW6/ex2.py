class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)
    
    def clear_list(self): #очищення списку✅
        self._length = 0
        self._head = None
        self._tail = None

    def fake_insert(self, index, element): # додавання елемента у довільне місце списку
        ... #не зрозумів як

    # def del_fom_lst(self, element= self._tail, index=None):
    #     if element in self:
    #         if index == None: 
    #             self._length -= 1
    #             self._tail = None
        
        

def main():
    my_list = MyList([1, 2, 5])
    print(my_list)

   
    my_list.clear_list()  #очищення списку✅
    print(my_list)

    # my_list.fake_insert() # додавання елемента у довільне місце списку
    # print(my_list)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    
    # my_list.del_fom_lst(3) # видалення елемента з кінця та довільного місця списку.
    # print(my_list)


if __name__ == '__main__':
    main()