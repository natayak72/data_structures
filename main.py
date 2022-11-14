
class MyClass:
    """
    FIFO

    Очередь имеет своё ограничение из-за того, что удаление из конца или вставка элемента в начало имеют сложность O(n).

    Чтобы обойти это ограничение, исп. следующие правила:

        1. Определим максимальную длину очереди — max_size.
        2. При переполнении будем запрещать добавление элементов в очередь.
        3. Зафиксируем два указателя:  head (начало) и tail (хвост) очереди.
        4. Закольцуем очередь таким образом, что если указатель tail >= max_size, то мы перемещаем его в начало
    """

    def __init__(self):
        try:
            self.max_size = int(input('Введите размер очереди: '))
        except ValueError:
            print('Введено не число! Использую размер по умолчанию: 5')
            self.max_size = 5
        if self.max_size < 0:
            print('Введено отрицательное число! Использую размер по умолчанию: 5')
            self.max_size = 5

        self._q = [0 for _ in range(self.max_size)]

        self.head = 0
        self.tail = 0
        self.cur = 0

    def is_empty(self):
        if self.head == self.tail and self._q[self.head] == 0:
            return True
        else:
            return False
        
    def is_full(self):
        if self.head == self.tail and self._q[self.head] != 0:
            return True
        else:
            return False

    def get_size(self):
        if self.is_empty():
            return 0
        elif self.head < self.tail:
            return self.tail - self.head
        elif self.tail < self.head:
            return self.max_size - self.head + self.tail
        else:
            return self.max_size


    def add(self):
        if self.is_full():
            print('Очередь полная. Не могу добавить.')
            return

        if self.is_empty():
            self.cur = self.tail

        self._q[self.tail] = 1
        self.tail += 1

        if self.tail == self.max_size:
            self.tail = 0
        


    def pop(self):
        if self.is_empty():
            print('Очередь пустая. Некого убирать.')
            return
        self._q[self.head] = 0
        self.head += 1
        self.cur = self.head

        if self.head == self.max_size:
            self.head = 0


    def get_cur(self):
        if self.is_empty():
            print('В данный момент задач нет.')
        else:
            print(f'Следующий по почереди {self.cur}')


    def print_my_class(self):
        print('\n')
        print('-----' * (self.max_size + 1))
        print(f'head: {self.head}')
        print(f'tail: {self.tail}')
        print(f'size: {self.get_size()}')

        header = 'i: '
        my_class = 'q: '
        for i in range(self.max_size):
            header += f'{i: ^5}'
        for i in self._q:
            my_class += f'{i: ^5}'

        print(header)
        print(my_class)
        print('\n')



def main():
    my_class = MyClass()

    while True:
        my_class.print_my_class()
        cmd = input('Команда: (add/pop/size/empty/cur) ')

        if cmd == 'empty':
            if my_class.is_empty():
                print('Очередь пустая.')
            else:
                print('Очередь не пустая!')
        elif cmd == 'size':
            print(f'Размер очереди: {my_class.get_size()}')
        elif cmd == 'add':
            my_class.add()
        elif cmd == 'pop':
            my_class.pop()
        elif cmd == 'cur':
            my_class.get_cur()
        else:
            print('Введите команду ещё раз')







if __name__ == '__main__':
    main()
