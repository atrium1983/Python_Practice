# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, 
# если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]		same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)
 
def same_by(funk, val):
    arr = list(filter(funk,val))
    if len(val) == len(arr):
        return True
    else:
        return False
    
    #     if funk(i) == 0:
    #         arr.append(i)
    # if len(val) == len(arr):
    #     return True
    # else:
    #     return False
        arr= arr.append(filter(funk_1,val))
    


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
    
"""_summary_
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]		same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)

# def same_by(characteristic, objects):
#     result_list = []
#     for num in objects:
#         if characteristic(num):
#             result_list.append(num)
#     if objects == result_list or result_list == []:
#         return True
#     return False

# def same_by(characteristic, objects):
#     result_list = list(map(characteristic, objects))
#     print(result_list)

#     if len(objects) == sum(result_list) or sum(result_list) == 0:
#         return True
#     return False

def same_by(characteristic, objects):
    result_list = list(filter(characteristic, objects))
    print(result_list)

    if objects == result_list or result_list == []:
        return True
    return False


values = [5, 7, 9, 3]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
"""