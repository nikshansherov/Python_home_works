# Задание №5 семинара 3. Список номеров нечетных.

my_list = [1, 3, 178, 333, 14, 34, 555, 8, 4, 9, 11]
new_list = []
count = 1

for item in my_list:
    if item % 2 != 0:
        new_list.append(count)
    count += 1

print(f'Исходный список: {my_list}')
print(f'Список номеров нечетных элементов: {new_list}')
