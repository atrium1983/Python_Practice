"""
Является ли число N числом Фибоначчи?
"""

import math

n = int (input("Введите число N => "))
if math.sqrt((5*(n**2) + 4)) % 1 == 0 or math.sqrt((5*(n**2) - 4)) % 1 == 0:
    print('Yes')
else:
    print('No')
    