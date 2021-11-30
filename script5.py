orientation = 0
<<<<<<< HEAD
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
=======
while True:
    print ("Куда хотите пойти: вверх, вниз, вправо или влево?")
    orientation = input()
    print ("На сколько шагов хотите сместиться?")
    step = int(input())
    if orientation == "вверх":
      x = 0
      y = step
      print('Ваши координаты: {0}:{1}'
          .format (x, y))
    elif orientation == "вниз":
      x = 0
      y = step * -1
      print('Ваши координаты: {0}:{1}'
      .format (x, y))
    elif orientation == "влево":
      x = step * -1
      y = 0
      print("Ваши координаты: {0}:{1}"
      .format (x, y))
    elif orientation == "вправо":
      x = step
      y = 0
      print("Ваши координаты: {0}:{1}"
      .format (x, y))
    elif orientation == "хватит":
      break
    else:
     print ("Вы неверо ввели ориентацию")
>>>>>>> 818754c6ffcd2bd1dacf45ffe3a10e0c491c57c2
