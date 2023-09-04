"""
Напишите программу для печати всех уникальных значений в словаре. 

Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально. Пользователь его не вводит
"""  

dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

set_value = []

for cur_dict in dict_1:
    for k in cur_dict.keys():
        set_value.append(cur_dict[k])

res_set = set(set_value)
print(res_set)
    
