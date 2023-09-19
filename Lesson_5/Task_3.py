# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# def prim_num_check(n):
#     for i in range (2, n//2 + 1):
#         if n% i == 0:
#             return False
#     return True
    
# check = prim_num_check(int(input('=> ')))
# if check: print("YES")
# else: print("NO")

#from seminar
def is_number_simple(num: int) -> bool:
    if num % 2 == 0 and num != 2:
        return False

    for i in range(3, int(num ** 0.5) +1, 2):
        if num % i == 0:
            return False
    return True

n = int(input('Введите число: '))
if is_number_simple(num=n):
    print(f'Число {n} является простым') 
else:
    print(f'Число {n} простым не является')