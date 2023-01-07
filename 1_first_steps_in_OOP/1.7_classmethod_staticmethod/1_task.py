"""
Подвиг 1. В программе объявлен следующий класс с одним методом:

class Stepik:
    def get_certificate(self):
        return False
И создается объект этого класса:

st = Stepik()
Выберите все верные варианты вызова метода get_certificate:
"""


class Stepik:
    def get_certificate(self):
        return False


st = Stepik()
print(Stepik.get_certificate(st))  # OK
print(st.get_certificate())  # OK

# print(get_certificate())
# name 'get_certificate' is not defined

# print(Stepik.st.get_certificate())
# type object 'Stepik' has no attribute 'st'

# print(st.Stepik.get_certificate())
# 'Stepik' object has no attribute 'Stepik'

# print(Stepik.get_certificate())
# get_certificate() missing 1 required positional argument: 'self'
