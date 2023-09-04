"""
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо, 
K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3 
Output: [3, 4, 5, 1, 2]
"""

n, k = int(input("Insert lenght = > ")), int(input("Insert shift = > "))

list_1 = [ i for i in range (1,n + 1)]
print(list_1)

# Решение через сдвиг (оптимальное)
# list_2 = list_1[-k:] + list_1[:-k]

# Решение через циклы
list_2 = []
for i in range (len(list_1) - k, len(list_1)):
    list_2.append(list_1[i])
for i in range (0, len(list_1) - k):
    list_2.append(list_1[i])
print(list_2)
    
