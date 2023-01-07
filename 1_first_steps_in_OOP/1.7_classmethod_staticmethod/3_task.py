"""
Подвиг 3. В программе объявлен следующий класс с одним методом:

class Math:
    @staticmethod
    def sqrt(x):
        return x ** 0.5
И создается объект этого класса:

m = Math()
Выберите все верные варианты вызова метода sqrt:
"""


class Math:
    @staticmethod
    def sqrt(x):
        return x ** 0.5


m = Math()

res = Math.sqrt(4)  # ОК

res = m.sqrt(2)  # OK

# print(m.Math.sqrt(3))
# 'Math' object has no attribute 'Math'

# res = Math.sqrt(m, 4)
# sqrt() takes 1 positional argument but 2 were given
