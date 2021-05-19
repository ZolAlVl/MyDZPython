# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

# persons = [{"name": "John",
# "age": 15},
# {"name": "Alison",
# "age": 28},
# {"name": "Tarantino",
# "age": 20},
# {"name": "Jack",
# "age": 45}]
#
# ages = []
# names_len = []
# for person in persons:
#     ages.append(person["age"])
#     names_len.append(len(person["name"]))
#
# min_age = min(ages)
# long_name_len = max(names_len)
# #a)
# for person in persons:
#     if person["age"] == min_age:
#         print(person["name"])
# #б)
# print("___________")
# for person in persons:
#     if len(person["name"]) == long_name_len:
#         print(person["name"])
#в)
# print("___________")
# mean_age = sum (ages) / len (ages)
# print(mean_age)
##########################################################################
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение},
# для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях
# - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

#а)
# my_dict_1 = {200:200, 500:500, 11:11, 8:8}
# my_dict_2 = {8:8, 100:100, 500:500, 20:20, 5:5}
#
# common_keys = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(common_keys)
#
# #б)
# first_keys = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# print(first_keys)
#
# #в)
# first_dict = {key: value for key, value in my_dict_1.items() if key in first_keys}
# print(first_dict)
#
# # г)
# res_dict = {**my_dict_1, **my_dict_2}
# for key in common_keys:
#     res_dict[key] = [my_dict_1[key], my_dict_2[key]]
# print(res_dict)
