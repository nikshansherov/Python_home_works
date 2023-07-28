from my_except import MyStringError


class User:
    def __init__(self, name, last_name):
        if not isinstance(name, str) or not name.isalpha():
            raise MyStringError(name)
        if not isinstance(last_name, str) or not last_name.isalpha():
            raise MyStringError(last_name)
        self.name = name
        self.last_name = last_name


u = User('Иван', 5)
print(u.name)
