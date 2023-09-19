# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

list_1 = "a a a b c a a d c d d"
list_2 = list_1.split()
dict ={}

for i in list_2:
    if i in dict:
        print(f'{i}_{dict[i]}', end=' ') 
    else: 
        print(i, end=' ')
    #dict[i] = dict.get(i,0) +1
    dict[i] = dict.setdefault(i, 0) +1


# решение 1 на семинаре с другой группой:

# list = 'a a a b c a a d c d d'.split()

# letters = []
# for i in list:
#     if i not in letters:
#         letters.append(i)

# print(letters)

# count = []
# print(count)

# for letter in letters:
#     num= 1
#     for elem in list:
#         if elem in letters:
#             print(elem, end=' ')
#             letters.remove(elem)
#         else:
#             print(f'{elem}_{num}', end=' ')
#             num+=1
#     count.append(num)



# # решение 2 на семинаре с другой группой:

# new = "a a a b c a a d c d d".split()
# print(new)
# dict_1 = {}

# for letter in new:
#     if  letter in dict_1:
#         dict_1[letter] += 1
#         print(letter + "_" + str(dict_1[letter]), end = " ")
#     else:
#         dict_1[letter] = 0
#         print(letter, end = " ")
        



     	

