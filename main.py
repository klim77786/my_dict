# Первая ветка задание 1-3

my_list = [42, 43]
my_dict = {
    'foo': {
        'a': 12,
        'b': (1, 2, 3, 4, my_list)
    },
    'bar': {
        'c': 12,
        'd': {5, 6, 7}
    },
    'moo': {
        'e': 12,
        'f': {'lol': ['l', 'o', 'l']}
    },
}
print(my_dict['foo'])
print(my_dict['foo'].get('b'))
my_list.append(44)

# Вторая ветка задание 4-6

print(my_dict['foo'].get('b'))
print(my_dict['bar'].get('d'))
my_dict['bar'].get('d').add(9)

# Третья ветка решение 7-10 задачи

print(my_dict['bar'].get('d'))
my_dict['moo'].get('f').get('lol').remove('o')
key = {'k': ['K', 'e', 'k']}
my_dict['moo'].get('f').update(key)
print(my_dict['moo'].get('f'))
my_dict.clear()
print(my_dict)



