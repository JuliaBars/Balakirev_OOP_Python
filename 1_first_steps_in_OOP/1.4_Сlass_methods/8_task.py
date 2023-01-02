"""
Подвиг 8. В программе объявлен класс:

class String:
    is_empty = False
А, затем, создаются два его экземпляра:

s1 = String()
s2 = String()
После этого выполняется команда:

s2.is_empty = True
Выберите верные утверждения, связанные с этой программой.
"""


class String:
    is_empty = False


s1 = String()
s2 = String()

s2.is_empty = True

# Выберите все подходящие ответы из списка: 4 верных ответа

# ВЕРНО
# Переменная a = s1.is_empty будет ссылаться на атрибут is_empty класса String
a = s1.is_empty
print(s1.__dict__)  # {} локальных атрибутов нет
print(a)  # но есть атрибут класса String

# НЕВЕРНО
# Значения s1.is_empty и s2.is_empty будут совпадать и принимать значение True
print(s1.is_empty == s2.is_empty)  # False, мы переопределили атрибут s2

# ВЕРНО
# Переменная b = s2.is_empty будет ссылаться на локальный атрибут
# is_empty объекта s2
b = s2.is_empty
print(b)  # True

# НЕВЕРНО
# Последняя команда изменит атрибут is_empty класса String на значение True
print(String.is_empty)  # False команда из объекта не меняет значение в классе

# ВЕРНО
# Значение s1.is_empty будет по-прежнему False, а значение s2.is_empty
# примет новое значение True
print(s1.is_empty, s2.is_empty)  # False True

# ВЕРНО
# Последняя команда создаст локальное свойство is_empty со значением
# True в экземпляре s2
print(s2.__dict__)  # {'is_empty': True}
