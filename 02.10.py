#Задача №1

# Запрос арифметического выражения
#expression = input("Введите арифметическое выражение (например, 23+12): ")
# Разбиение выражения на числа и оператор
#parts = expression.split()
#if len(parts) == 3:
#   num1 = float(parts[0])
#   operator = parts[1]
#   num2 = float(parts[2])  
#   # Вычисление результата
#   if operator == '+':
#       result = num1 + num2
#   elif operator == '-':
#       result = num1 - num2
#   elif operator == '*':
#       result = num1 * num2
#   elif operator == '/':
#       if num2 == 0:
#           print("Ошибка: деление на ноль.")
#       else:
#           result = num1 / num2
#   else:
#       print("Ошибка: неверный оператор.")
#else:
#   print("Ошибка: неверный формат ввода.")
# Вывод результата
#print("Результат:", result)




#Задача №2

#from random import randint
#l = [randint(-10,10) for i in range(20)]
#def f(e):
#    return e < 0
#n = l.count(0)
#p = list(filter(f,l))
#print(l)
#print('максимальное', max(l))
#print('минимальное',min(l))
#print('нулей:',n)
#print('положительных',len(l) - len(p) - n)
#print('отрицательных',len(p))