#Работа со списками
my_list = ['apple', 'carrot', 'corn', 'cherry', 'pineapple', 'orange']
print(my_list)
print('Первое слово:', my_list[0], '   Последнее слово:', my_list[len(my_list)-1])
print(my_list[2:5])
my_list[2] = 'mushroom'
print(my_list)
#Работа со словорями
my_dict = {'apple': 'яблоко', 'carrot': 'морковь', 'corn': 'кукуруза', 'cherry': 'вишня', 'pineapple': 'ананас',
           'orange': 'апельсин'}
print(my_dict)
print('Перевод:', my_dict[input()])
my_dict.update({input(): input()})
print(my_dict)
