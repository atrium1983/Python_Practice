import os
os.system('cls')



import random

N = 10
array = []
for i in range(N):
    array.append(random.randint(-10, 9))
print(array)
 

 
for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                max = array[j]
                array[j] = array[j+1]
                array[j+1] = max

print(array)


n = int(input("Введите число N => "))



num = 1
for i in range (N-1):
    if array[i] != array[i+1]:
        num += 1

print(num) 



# Random list creation

import random, os
os.system('cls')

n = int(input('Введите кол-во элементов в списке = > '))

list_1 = [n]

for i in range (n):
    list_1 = [random.randint(0, 10) for _ in range (n)]

print(*list_1, sep=", ")