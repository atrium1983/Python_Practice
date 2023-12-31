"""
Задача 4
Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
(при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
что без дополнительной информации это сделать невозможно.
Input: 3 4(ввод на разных строках) Output: 6
"""
import os
os.system('cls')

i = int(input('Insert vagon number starting from the head of the train '))
j = int(input('Insert vagon number in the ticket '))
if i > j:
    print(f"Train has {i - 1 + j} vagons")
elif i == j:
    print("Not enough information to calculate number of vagons")
else:
    print(f"Train has {j - 1 + i} vagons")