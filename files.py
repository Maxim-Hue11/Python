# dict1 = {
#     "name": "Вася", 
#     "age": 5,
#     }

# dict2 = {
#     "name": "Вася", 
#     "age": 5,
#     'color': "red"
#     }

# print(dict2['color'])
# print(dict1['color'])

# print(dict2.get('color'))
# print(dict1.get('color'))

# dict = {
#     "name": "Вася", 
#     "age": 5,
#     }

# dict.update( {"cars": ["Мазда", "Тойота"]})
# dict["height"] = 176
# x = 'age'
# dict[x] = 7

# print(dict['cars'][1])
# print(dict)


# Задача 1 
#  у вас есть словарь из 5 имен/ возрастов 
#               где ключ это имя а возраст - значение
#  пользователь введет имя человека - выведите его возраст
#  ввод в цикле вайл тру 
#  если человека нет в списке выведите "НЕТУ ТАКОГО"

# dict = {
#     "Masha": 15,
#     "Dasha": 44,
#     "Pasha": 33,
#     "Vasha": 22,
#     "Gasha": 11,
# }

# while True:
#     name = input("Enter name: ")
#     if dict.get(name) == None:
#         print('NO') 
#         break
#     print(dict.get(name))

# Задача 2
#  у вас есть пустой словарь 
#               где ключ это имя а возраст - значение
#  пользователь введет имя человека , 
#                   затем возраст добавьте их в список
#  после каждого ввода выведите 
#               человека с самым большим возрастом 
#  ввод в цикле вайл тру 

dict = { }
   

while True:
    name = input("Введи любое имя: ")
    age = int(input("Введи возраст этого человека: "))

    dict[name] = age

    print(dict)
    print("Человек с самым большим возрастом: ",max(dict))