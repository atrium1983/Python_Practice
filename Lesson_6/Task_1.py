# Задача 39
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива.

# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)
import random

#n = int(input("Введите кол-во элементов 1 массива => "))
#list_1 = [int(input("Введите число => ")) for _ in range (n)]
n = random.randint(5,10)
list_1 = [random.randint(1,10) for _ in range (n)]

#m = int(input("Введите кол-во элементов 2 массива => "))
#list_2 = [int(input("Введите число => ")) for _ in range (m)]
m = random.randint(5,10)
list_2 = [random.randint(1,10) for _ in range (m)]

print(*list_1)
print(*list_2)

list_3 = [elem for elem in list_1 if elem not in list_2]
# list_3 = []
# for elem in list_1:
#     if elem not in list_2:
#         list_3.append(elem)
print(*list_3)