# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) 
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в 
# массиве. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5    6
#     -> 5
list= []
print("Введите количество эллментов массива :")
n = int(input())
from random import randint
for i in range(n):
   list.append(randint(1, n)) 
print(list)
print("Введите значение х :")
x = int(input())
list_new =[abs(x-i) for i in list]
print(list[list_new.index(min(list_new))])