#print ('Введите два числа');
#(first, second) = input().split()
#print('Сложение: {0} Вычитание: {1} Уможение: {2} Деление: {3} Степень: {4} Целочисленное деление: {5} Модуль: {6}'
#.format ((float(first) + float(second)), (float(first) - float(second)),(float(first) * float(second)),(float(first) / float(second)), (float(first) ** float(second)),(float(first) // float(second)),(float(first) % float(second))))


print("Введите два числа ")
a = 5
b = 5
def sum(a, b):
    return a + b
def diff(a, b):
    return a - b
def multi(a,b):
    return a * b
def division(a,b):
    return a / b
def degree(a,b):
    return a ** b
def mod(a,b):
    return a // b
