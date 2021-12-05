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
