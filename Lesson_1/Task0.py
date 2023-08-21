'''
Сравнить два числа
'''

first = int(input ('Insert first number '))
second = int(input ('Insert second number '))
if first > second:
    print (f"First = {first} > second = {second}")
elif first == second:
    print (f"First = {first} = second = {second}")
else: 
    print (f"First = {first} < second = {second}")