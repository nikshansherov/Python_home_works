# Задание №8 семинара 1. Елка.

num = int(input('Введите количесво рядов елки: '))

for i in range(1, num + 1):
    print((num - i) * ' ', (2 * i - 1) * '*')