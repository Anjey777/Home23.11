# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
# не (x или y или z) = не x и не y и не z

X = [True, False]
Y = [True, False]
Z = [True, False]
for x in X:
    for y in Y:
        for z in Z:
            print(x, y, z)
            result1 = not (x or y or z)
            result2 = (not x) and (not y) and (not z)
            print(result1 == result2)
