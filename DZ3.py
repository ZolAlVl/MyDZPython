value = 50
result = value / 2 if value < 100 else -value
print (result)
############################################################
value = 107
result = "1" if value < 100 else "0"
print(result)
# ##########################################################
value = 120
result = "True" if value < 100 else "False"
print(result)
#########################################################
my_str = "Hello, World!"
print(my_str[::2])
#########################################################
my_str = "Hello, World!"
print(my_str[1::2])
##########################################################
my_str = "Привет,друг"
my_str = my_str + my_str if len(my_str) < 5 else my_str
print (my_str)
#########################################################
my_str = "Хай"
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print (my_str)





