#     Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
#    Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Введите координаты точки')
x = int(input('x= '))
y = int(input('y= '))
if x > 0 and y > 0:
    print('Точка лежит в 1 четверти')
elif x < 0 and y > 0:
    print('Точка лежит во 2 четверти')
elif x < 0 and y < 0:
    print('Точка лежит в 3 четверти')
elif x > 0 and y < 0:
    print('Точка лежит в 4 четверти')
elif x == 0 and y == 0:
    print('Точка лежит в центре координат')
elif x == 0:
    print('Точка лежит в 0 оси У')
elif y == 0:
    print('Точка лежит в 0 оси Х')
