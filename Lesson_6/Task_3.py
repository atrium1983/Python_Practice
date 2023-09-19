# Задача 43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод: 
# 1 2 3 2 3
    
# Вывод:
# 2

from random import randint
import os
os.system('cls')

n = randint(5,10)
list_1 = [randint(1,10) for _ in range(n)]
print(*list_1)

# 1. моё решение (для 10 элементов - 38 шагов):

#   count = 0         
# for i in range (n):
#     if list_1.count(i) == 2:
#         count += 1
#print(count)

# 2. решение с семинара (для 10 элементов - 93 шагов):
# count = 0
# for i in range(n-1):
#     for j in range (i+1,n):
#         if list_1[i] == list_1[j]:
#             count += 1
#print(count)

# 3. Решение через словарь (для 10 элементов - 62 шага). Можно найти пары, 
# если число повторяется на 2 а более раз (4)):
list_1 = str(list_1).strip('[]').replace(',' , '').split()
print(list_1)
dict_1 = {}
for i in list_1:
    dict_1[i] = dict_1.get(i, 0) +1
print(dict_1)
count = 0
for k,v in dict_1.items():
    if v >= 2:
        count += int(v/2)
print(count)