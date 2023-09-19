# Задача 45
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300 
# Вывод: 220 284

def sum_divisors(number):
    sum = 1
    for div in range (2,int(number**0.5)+1):
        if number%div == 0:
            sum += div + number//div
    return sum

def search_divisor(number: int) -> list:
    divisors = [div for div in range (1,number//2+1) if number%div == 0]
    return divisors

def sum_elements(list_to_sum: list) -> int:
    sum = 0
    for i in list_to_sum: 
        sum += i
    return sum

def find_friends_numbers(number: int):
    friends_num_list = []
    for num_to_try in range(1, number):
        # m = sum_elements(search_divisor(num_to_try))
        # n = sum_elements(search_divisor(m))
        m = sum_divisors(num_to_try)
        n = sum_divisors(m)
        if n == num_to_try and n != m:
            tuple_1 = (n,m)
            tuple_2 = (m,n)
            if tuple_2 not in friends_num_list:
                friends_num_list.append(tuple_1)
    return friends_num_list
        
k = int(input("Ведите число = > "))
# print(*search_divisor(k))
# print(sum_elements(search_divisor(k)))
# print(sum_divisors(k))
print(*find_friends_numbers(k))

