# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
immutable_var=(1,9,7,1,'year of birth',True)
print('Immurtable tuple: ', immutable_var)
# 2. Задайте переменные разных типов данных:
#  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# - Выполните операции вывода кортежа immutable_var на экран.
#immutable_var[3]=0 TypeError: 'tuple' object does not support item assignment
# Нельзя заменить элемент непосредственно в кортеже
# Но, если кортеж содержит в себе список, то элемент в списке уже можно изменить
# immutable_var=([1,9,7,1],'year of birth',True) # формируем кортеж, содержащий список с элементами 1,9,7,1.
# print('Immurtable tuple: ', immutable_var) # выводим - Immurtable tuple:  ([1, 9, 7, 1], 'year of birth', True)
# immutable_var[0][3]=0 #заменяем элемент равный 1 в списке на 0
# print('Immurtable tuple: ', immutable_var) # выводим - Immurtable tuple:  ([1, 9, 7, 0], 'year of birth', True)
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.
mutable_list=['Bioody Mary','vodka','tomato juice','Worcestershire Sauce', 'Tobasco Sauce', 'lemon juice','salt','black pepper', 15, 45, 90, 'coctail', True]
mutable_list.extend(['Queen of England',2])
print('Mutable list: ', mutable_list)
