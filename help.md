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




list = "a a a b c a a d c d d"
list_2 = list.split() 
print(list_2)
dict = {}

for i in list_2:	
    if i in dict:     	
        print(f'{i}_{dict[i]}', end=' ') 	
    else:     	
        print(i, end=' ') 
    dict[i] = dict.get(i,0) + 1 

print(dict)



a = "She sells sea shells on the sea shore; The shells that she sells are sea shells Im sure. So if she sells sea shells on the sea shore, Im sure that the shells are sea shore shells."
aa = a.lower()
b_new = aa.replace(('.' and ';'), '')
print(b_new)
c = b_new.split(' ' or '  ' or '   ')
d = set(c)
print(d)