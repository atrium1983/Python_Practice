"""
Задача 1
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
n = 700 m = 750 Output: 2
"""
import os
os.system('cls')

n = int(input('How many km pass the car per day => '))
m = int(input('Insert distance => '))
days = - (-m//n)
print(days)
