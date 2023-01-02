"""
Подвиг 9. Из входного потока читаются строки данных в формате:
id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:

select(self, a, b) - возвращает список из элементов списка lst_data в
диапазоне [a; b] (включительно) по их индексам (не id, а индексам списка);
также учесть, что граница b может превышать длину списка.
insert(self, data) - для добавления в список lst_data новых данных из
переданного списка строк data;

Каждая запись в списке lst_data должна быть представлена словарем в формате:

{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например:

{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

Примечание: в этой задаче число элементов в строке (разделенных пробелом)
всегда совпадает с числом полей в коллекции FIELDS.

P. S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
"""


import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        return self.lst_data[a: b + 1]


db = DataBase()
db.insert(lst_in)

# ничего выводить на экран не нужно, это лишь для наглядного примера работы
# [{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'},
# {'id': '2', 'name': 'Федор', 'old': '23', 'salary': '12000'},
# {'id': '3', 'name': 'Иван', 'old': '13', 'salary': '1200'}] 
print(db.lst_data)