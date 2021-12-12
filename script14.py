''' задача 2. commit 2
     print ('Введите два числа');
    (first, second) = input().split()
    print('Сложение: {0} Вычитание: {1} 
           Уможение: {2} Деление: {3} 
           Степень: {4} Целочисленное деление: {5} 
           Модуль: {6}'
    .format ((float(first) + float(second)),
            (float(first) - float(second)),
            (float(first) * float(second)),
            (float(first) / float(second)), 
            (float(first) ** float(second)),
            (float(first) // float(second)),
            (float(first) % float(second))))'''
''' Задача 3. commit 2
     print ('Введите Ваше имя')
         name = input ()
     print('Здравствуйте, {0}!'
         .format (name))
'''
''' Задча 4. commit 3
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
'''
''' Задача 5. commit 3
     orientation = 0
     stop = 'хватит'
         while True:
                 print ("Куда хотите пойти: вверх, вниз, вправо или влево?")
                     orientation = input()
                 print("На сколько шагов хотите сместиться?")
                     step = int(input())
                     x = 0
                     y = 0
             if  orientation == 'вверх':
                     x = 0
                     y = step 
                print ('Ваши координаты: {0}:{1}'
                     .format (x, y))
             elif orientation == 'вниз':
                     x = 0
                     y = step * -1
                 print ('Ваши координаты: {0}:{1}'
                     .format (x, y))
             elif orientation ==  'вправо':
                     x = step
                     y = 0
                 print ('Ваши координаты: {0}:{1}'
                 .format (x, y))
             elif orientation == 'влево':
                     x = step * -1
                     y = 0
                  print ('Ваши координаты: {0}:{1}'
                     .format (x, y))
             else:
                 print('Вы неверно ввели ориентацию')
 
'''
'''Задача 6 commit 4
     from random import randint
         N = 5
         a = []
     for i in range(N):
         a.append(randint(1, 99))
         print(a)
     for i in range(N-1):
         for j in range(N-i-1):
             if a[j] > a[j+1]:
                 a[j], a[j+1] = a[j+1], a[j]
         print(a)
'''
'''Задча 7 commit 4
     dict_color = { 'red':(255, 0, 0), 'Lime':(0, 255, 0),
                  'LightSeaGreen':(32, 178, 170), 'Tomato':(255, 99, 71), 
                  'Cyan':(0, 255, 255), 'Orchid':(218, 112, 214), 
                  'Blue':(0, 0, 255), 'Chocolate':(210, 105, 30)}
     print (dict_color)
         x = dict_color['Lime']
             print (x)
'''
'''задача 8 commit 4
     from random import sample
         list = sample(range(10, 110), 20)
         list1 = sample(range(10, 110), 20)
         valuew = []
             a = set(list)
             b = set(list1)
                 s = a.intersection(b) #входят одновременно в оба 
                 d =  a.difference(b) #входят в первое, но не входят во второе
                 f = b.difference(a) #входят во второе, но не входят в первое
                 g = a.symmetric_difference(b) #встречаются в одном, но не в обоих
         print("первый набор", a)
         print("второй набор",b)
         print("входят одновременно в оба", s)
         print ("входят в первое, но не входят во второе",d)
         print("входят во второе, но не входят в первое",f)
         print("встречаются в одном, но не в обоих",g)
'''
''' Задача 9 commit 5
     import re
         # определение пользовательских исключений
         class Error(Exception):
             """Базовый класс для других исключений"""
        pass
         class ValueTooSmallError(Error):
             """Вызывается, когда входное значение меньше 6"""
         pass
         class ValueTooPass(Error):
             """Вызывается, когда входной пароль состоит из слова password"""
         pass
         class ValueTooDigit(Error):
             """Вызывается, когда входной пароль состоит только из цифр"""
         pass
         class ValueTooOneDigit(Error):
             """Вызывается, когда входной пароль не содержит цифр вообще"""
         pass
     print("Введите Ваш пароль: ")
         passw = input()
             def func1(passw):
                 try:
             if len(passw) < 6:   #Проверка не менее 6 символов
                 raise ValueTooSmallError
             elif passw.isdigit(): # Проверка "Не должен состоять только из цифр"
                 raise ValueTooDigit
             elif passw == 'password' or passw == 'PASSWORD':
                 raise ValueTooPass
             #elif passw := re.compile(r'^(?=.*[0-9].*)$'):
                 #Вот с этим проблема, прочитала про возможность использования регулярок, ничего не вышло.. не смогла придумать как исправить.
                 #(?=.*[0-9]) - строка содержит хотя бы одно число; 
                 # raise ValueTooOneDigit
             else:
                 print ("Крутой надежный пароль!")
             except ValueTooSmallError:
                 print("Пароль не может быть менее шести символов!!\n")
             except ValueTooDigit:
                 print("Пароль не должен состоять только из цифр!\n")
             except ValueTooPass:
                 print("Пароль не должен быть password!\n")
             except ValueTooOneDigit:
                 print("Пароль должен содержать хотя бы одну цифру!\n")
         x = func1(passw)
             print(x)
'''
''' Задача 10 commit 5
     def adder(*nums):
         sum = 0
     for n in nums:
         sum += n
     print("Cумма полученных аргументов ", sum)
         adder(4, 5, 6, 7)
         adder(1, 2, 3, 5, 6)
         adder(1,2,3,4,5)
 '''
''' Задача 11 commit 6
    Rainbow = ['Аня', 'Осипова', 'люблю', 'Тензор', 'и', 'программировать', 'хыхы']
      print('Кодирование строки:')
      print(Rainbow[0].encode('utf-8'))
      print('Декодирование строки:')
      print(b'\xd0\x90\xd0\xbd\xd1\x8f'. decode('utf-8'))

'''
''' Задача 12 commit 6
     print("Введите количество атомов")
         C, H, O = map(int, input().split())
             y = open('input.txt', 'w')
                 print(y.write(str(C)))
                 print(y.write(str(H)))
                 print(y.write(str(O)))
         C = C //2
         H = H//6
         x =  min(C,H,O)
             f = open('output.txt', 'w')
                 print(f.write(str(x)))
             f.close
'''

