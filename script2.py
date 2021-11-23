print ('Введите два числа');
(first, second) = input().split()
print('Сложение: {0} Вычитание: {1} Уможение: {2} Деление: {3} Степень: {4} Целочисленное деление: {5} Модуль: {6}'
.format ((float(first) + float(second)), (float(first) - float(second)),(float(first) * float(second)),(float(first) / float(second)), (float(first) ** float(second)),(float(first) // float(second)),(float(first) % float(second))))
