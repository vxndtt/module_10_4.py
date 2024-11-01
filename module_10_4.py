import queue
import threading
import time
from queue import Queue
from random import randint
from threading import Thread

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('Hi')
        return time.sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    self.queue.get(guest)
                else:
                    self.queue.put(guest)
                    print(f'{table.guest.name} в очереди')

    def discuss_guests(self):
        if not queue.Empty():
            for table in tables:
                if table.guest is not None and not Thread.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла')
                    print(f'{table.number} свободен')
                    table.guest = None
                else:
                    if table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()