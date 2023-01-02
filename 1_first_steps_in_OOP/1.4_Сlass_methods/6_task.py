"""
Подвиг 6. Имеется следующий класс:

class Stepik:
    def next_task(self):
        return "Следующее задание"
И создается объект этого класса:

my_st = Stepik()
Выберите все верные варианты вызова метода next_task()
"""


class Stepik:
    def next_task(self):
        return "Следующее задание"


my_st = Stepik()

print(Stepik.next_task(my_st))
# Следующее задание

print(Stepik.my_st.next_task())
# AttributeError: type object 'Stepik' has no attribute 'my_st'

print(next_task(Stepik)) 
# NameError: name 'next_task' is not defined

print(my_st.next_task(Stepik))
# TypeError: next_task() takes 1 positional argument but 2 were given

print(next_task(my_st))
# NameError: name 'next_task' is not defined

print(my_st.next_task())
# Следующее задание
