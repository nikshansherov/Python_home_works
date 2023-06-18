# Задание №8 семинара 3. Множества.

friends = {'friend_1': ('соль', 'хлеб', 'консерва', 'спички', 'спининг', 'термос', 'сигареты'),
           'friend_2': ('сахар', 'кружка', 'консерва', 'крупа', 'ложка', 'зажигалка', 'сигареты'),
           'friend_3': ('удочка', 'ложка', 'чай', 'вилка', 'пиво', 'спички', 'сигареты')}

for key in friends.keys():
    if key == 'friend_1':
        set_1 = set(friends[key])
    elif key == 'friend_2':
        set_2 = set(friends[key])
    else:
        set_3 = set(friends[key])

set_all = set_1 & set_2 & set_3
print(f'все друзья взяли {set_all}')

set_un_1 = set()
for item in set_1:
    if item not in set_2 | set_3:
        set_un_1.add(item)
print(f'{set_un_1} есть только у первого друга')

set_un_2 = set()
for item in set_2:
    if item not in set_1 | set_3:
        set_un_2.add(item)
print(f'{set_un_2} есть только у второго друга')

set_un_3 = set()
for item in set_3:
    if item not in set_1 | set_2:
        set_un_3.add(item)
print(f'{set_un_3} есть только у третьего друга')

set_not_1 = set()
for item in set_2 & set_3:
    if item not in set_1:
        set_not_1.add(item)
print(f'у второго и третьего друга есть {set_not_1}, а у первого нет')

set_not_2 = set()
for item in set_1 & set_3:
    if item not in set_2:
        set_not_2.add(item)
print(f'у первого и третьего друга есть {set_not_2}, а у второго нет')

set_not_3 = set()
for item in set_1 & set_2:
    if item not in set_3:
        set_not_3.add(item)
print(f'у первого и второго друга есть {set_not_3}, а у третьего нет')
