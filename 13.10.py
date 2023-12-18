num1 = int(input("введите число 1\n"))
num2 = int(input("введите число 2\n"))
num3 = int(input("введите число 3\n"))
all = [num1, num2, num3]

c = int(input("выберите действие: 1 найти максимум, 2 найти минимум, 3 найти среднее \n"))

if c == 1:
    print ('Максимум из 3х:', max(all))
elif c == 2:
    print ('Минимум из 3х:', min(all))
elif c == 3:
    print('Среднее из 3х:', sum(all) / len(all))
else:
    print("введите число от 1 до 3")