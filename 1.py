# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
day = int(input('Введите день: '))
if day == 1:
    print('Понедельник - не выходной')
elif day == 2:
    print('Вторникне - не выходной')
elif day == 3:
    print('Среда - не выходной')
elif day == 4:
    print('Четверг - не выходной')
elif day == 5:
    print('Пятница - не выходной')
elif day == 6:
    print('Суббота - выходной')
elif day == 7:
    print('Воскресение -  выходной')
else:
    print('В неделе всего семь дней')

# Вариант два
# day = int(input('Введите число дня недели: '))
# if 1 <= day <= 5:
#    print("Нет")
# elif 6 <= day <= 7:
#    print("Да")
# else:
#    print("В неделе 7 дней")
