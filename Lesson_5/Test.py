# def fib(n):
# if n == 0:
#     return 0
# elif n in [1,2]:
#     return 1
# return fib(n - 1) + fib(n - 2)

# import function_file

# list_1 = []
# for i in range (0,10):
#     list_1.append(function_file.fib(i))
# print(list_1)

# print(function_file.quicksort([10, 5, 2, 3]))

# nums = [38, 27, 43, 3, 9, 82, 10]
# function_file.merge_sort(nums)
# print(nums)

import random

def min_serch (array):
    min = array[0]
    for i in array:
        if i < min:
            min = i
    return min

def max_serch (array):
    max = array[0]
    for i in array:
        if i > max:
            max = i
    return max

def max_to_min_change (array):
    min = min_serch(array)
    max = max_serch(array)
    for i in range (len(array)):
        if array[i] == max:
            array[i] = min
    return array

list_1 = [random.randint(1,5) for _ in range (5)]
print(list_1)

print(max_to_min_change(list_1))

