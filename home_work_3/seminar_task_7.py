# Задание №7 семинара 3. Count.

my_str = input('Введите строку: ')
print(my_str)
my_str = my_str.lower()
my_str = my_str.replace(' ', '')
my_dict1 = {}
my_dict2 = {}

for item in my_str:
    counter = 0
    if item == ' ':
        continue
    for element in my_str:
        if item == element:
            counter += 1
    my_dict1[item] = counter

for item in my_str:
    if item == ' ':
        continue
    quantity = my_str.count(item)
    my_dict2[item] = quantity

print('Словарь сформированный без использования функции count:', '\n', my_dict1)
print('Словарь сформированный с использованием функции count:', '\n', my_dict2)
