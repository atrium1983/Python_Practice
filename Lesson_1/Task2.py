"""
Задача 2
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
"""
import os
os.system('cls')

a = int(input('Insert number of kids in first class => '))
b = int(input('Insert number of kids in second class => '))
c = int(input('Insert number of kids in third class => '))
tables = -(-a//2 + (-b//2) + (-c//2))

print(tables)