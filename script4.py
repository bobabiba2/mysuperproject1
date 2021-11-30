print ("Куда хотите пойти: вверх, вниз, вправо или влево?")
orientation = input()
print("На сколько шагов хотите сместиться?")
step = int(input())
x = 0
y = 0
if  orientation == 'вверх':
    x = step
    y = 0
    print ('Ваши координаты: {0}:{1}'
    .format (x, y))
elif orientation == 'вниз':
    x = step * -1
    y = 0
    print ('Ваши координаты: {0}:{1}'
    .format (x, y))
elif orientation ==  'вправо':
    x = 0
    y = step
    print ('Ваши координаты: {0}:{1}'
    .format (x, y))
elif orientation == 'влево':
    x = 0
    y = step * -1
    print ('Ваши координаты: {0}:{1}'
    .format (x, y))
else:
    print('Вы неверно ввели ориентацию')