# # Задания:
# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

# my_list = [150, 300, 25, 80, 8]
# for value in my_list:
#     if value > 100:
#         print (value)
######################################################
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

# my_list = [150, 300, 2589, 25, 80, 8]
# my_results = []
# for value in my_list:
#     if value > 100:
#         my_results.append(value)
# print(my_results)
#######################################################
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

# my_list = [150, 300, 2589, 25, 80, 8]
# if len(my_list) < 2:
#     my_list.append(0)
# else:
#     last_value = my_list[-1] + my_list [-2]
#     my_list.append(last_value)
# print(my_list)
############################################################
# 4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.

# my_string = "0123456789"
# result = []
# for value_1 in my_string:
#     for value_2 in my_string:
#         result.append(int(value_1 + value_2))
# print(result)