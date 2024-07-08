immutable_var = (1, 2, 3, True, 'Name')
print('Immutable tuple: ', immutable_var)
# immutable_var.append(4) невозможное действия потому что у переменной <class 'tuple'>
mutable_list = [1, 2, 3, True, 'One']
print('Mutable list: ', mutable_list)
mutable_list[4] = 'New'
print('Mutable list: ', mutable_list)