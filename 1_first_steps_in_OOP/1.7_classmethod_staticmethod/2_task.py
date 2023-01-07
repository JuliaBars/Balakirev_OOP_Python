"""
Подвиг 2. В программе объявлен следующий класс с одним методом:

class Loader:
    @classmethod
    def json_parse(cls):
        return ""
И создается объект этого класса:

ld = Loader()
Выберите все верные варианты вызова метода json_parse:
"""


class Loader:
    @classmethod
    def json_parse(cls):
        return ""


ld = Loader()


# print(ld.json_parse(Loader))
# json_parse() takes 1 positional argument but 2 were given

print(Loader.json_parse())  # ОК


res = Loader.json_parse()  # ОК
print(res)

res = ld.json_parse()  # ОК
print(res)

print(ld.json_parse())  # ОК

# print(Loader.json_parse(ld))
# json_parse() takes 1 positional argument but 2 were given