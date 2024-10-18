my_dict = {'alex' : 2006, 'dima' : 2003}
print(my_dict)
print(my_dict['alex'])
print(my_dict.get('danila'))
my_dict.update({'ivan' : 1995, 'egor' : 2001})
u = my_dict.pop('ivan')
print(u)
print(my_dict)

my_set = {1, 2, 4, 4, 2, 1, 5, 5, True, 'target', "target",}
print(my_set)
my_set.add(6)
my_set.add(7)
my_set.discard(4)
print(my_set)