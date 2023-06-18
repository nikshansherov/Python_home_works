# Задание №6 семинара 3. Работа с выводом строки.

my_str = input('Введите строку: ')
my_str = my_str.split()
my_str = sorted(my_str)
len_max = 0
counter = 1

for item in my_str:
    if len(item) > len_max:
        len_max = len(item)

for item in my_str:
    print(str(counter), ' ', (len_max - len(item)) * ' ', item, sep='')
    counter += 1
