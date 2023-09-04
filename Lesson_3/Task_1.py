"""
Задача No17. Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

"""

import random

N = 10
list = []
for i in range(N):
    list.append(random.randint(-5, 4))
print(list)

# Решение через множества 1

list_2 = set(list)

# Решение через списки

'''
list_2 = []

for i in list: 
    if i not in list_2:
        list_2.append(i)
'''

#list_2 = [i for i in list if i not in list_2]
        
print(list_2)

print(len(list_2))