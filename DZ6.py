# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
# my_list = ['bubbles', 'qwe', 'letters']
# my_list_2=[]
# for index,letter in enumerate(my_list):
#     if index%2!=0:
#         my_list_2.append(letter[::-1])
#     else:
#         my_list_2.append(letter)
# print(my_list_2)
# ##################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# my_list = ['always', 'angry', 'fabulous','tomorrow','apple']
# my_list_2 = [letter for letter in my_list if letter [0] == 'a']
# print(my_list_2)
###############################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# my_list = ['always', 'angry', 'fabulous','tomorrow','apple']
# my_list_2 = [my_list_2 for my_list_2 in my_list if "a" in my_list_2]
# print(my_list_2)
##################################################################
# 4. Дан список my_list в котором могут быть как строки (type str)
# так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
# my_list = ['qwe', '2', 'wasd', 245678, 2589]
# my_list_2= [value for value in my_list if type(value) == str]
# print(my_list_2)
###################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
# my_str = 'qqwweeerty'
# my_new_str= [letter for letter in my_str if my_str.count(letter) == 1]
# print(my_new_str)
####################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# my_list=['qwe', '2', 'wasd']
# my_list_2=[245678, 'qwe','wasd', 'alpha']
# my_new_list= list(set(my_list) & set(my_list_2))
# print(my_new_list)
##################################################################
# 7. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках,
# но в каждой только по одному разу.
# my_list = ['qwe', '2', 'wasd']
# my_list_2 = [245678, 'qwe','wasd','alpha']
# print(list(set(my_list).intersection(my_list_2)))
########################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность


# person = {"Фамилия": "Прилучный",
#           "имя": "Олег",
#           "возраст": "38",
#           "проживание":{"страна": "Украина",
#                         "город": "Херсон",
#                         "улица": "Победы, 28"},
#           "работа": {"наличие": "есть работа",
#                      "должность": "учитель"}}
# print(person)
#################################################################
# # 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# # придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
        
        
# components = {"Составляющие:"
#               "Коржи": "Мука,800 г",
#               "Молоко": "500 мл",
#               "Масло": "100 г",
#               "Яйцо": "8 штук",
#               "Крем": {"Сахар": "400 г",
#                       "Масло": "100 г",
#                       "Ваниль": "щепотка",
#                       "Сметана": "500 г"},
#               "Глазурь": {"Какао": "5 ложек",
#                       "Сахар": "200 г",
#                       "Масло": "100 г" }}
# print(components)

