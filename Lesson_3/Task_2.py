"""
Задача No19. Решение в группах
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
K – положительное число.
Input: [1, 2, 3, 4, 5] k = 2 
Output: [4, 5, 1, 2, 3]
"""

# list_1 = [1, 2, 3, 4, 5]

n, k = int(input("Insert length of list = > ")), int(input("Insert shift number = > "))
list_1 = [i for i in range (1, n+1)]
print(list_1)

list_2 = []
list_2 = list_1[-k:] + list_1[:-k]

print(list_2)
    
