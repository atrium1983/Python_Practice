# 2) - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса 
# и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

def find_farthest_orbit(orbits):
    sqr_planet = []
    for sqr in orbits:
        sqr_planet.append(3.14 * sqr[0] * sqr[1])
    index_planet = sqr_planet.index(max(sqr_planet))
    return(orbits[index_planet])
    
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))


# def find_farthest_orbit(list_of_orbits):
#     pi = 3.14
#     # list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
#     list_of_orbits = list(filter(lambda pair: pair[0] != pair[1], list_of_orbits))
#     areas_list = [pair[0] * pair[1] * pi for pair in list_of_orbits]
#     max_area = max(areas_list)
#     max_area_index = areas_list.index(max_area)
#     return list_of_orbits[max_area_index]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))