# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 4 -> 3 4 8 6
# Output: 6 8 4 3

import random

def reverse (n):
    if n == 0:
        return ""
    #num = random.randint(1,10)
    #line = input("Insert number => ")
    line = str(random.randint(1,10))
    print(f'{line}', end=' ')
    return reverse(n-1) + line + " "
    
n = int(input("Введите количество чисел => "))
print(f'\n{reverse(n)}')



# n = int(input("Введите количество чисел > "))

# def print_numbers(n: int):
#     if n == 0:
#         return ""
#     line = input("Введите число > ")
#     return print_numbers(n - 1) + line + " "

# print(print_numbers(n).strip())
    
    