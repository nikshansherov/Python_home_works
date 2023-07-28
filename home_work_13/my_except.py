class MyException(Exception):
    pass


class MyValueError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Недопустимое значение стороны прямоугольника: {self.value} \n' \
               f'Значение должно быть положительным числом '


class MyStringError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Введено недопустимое значение: {self.value} \n' \
               f'Значение должно быть текстом'
