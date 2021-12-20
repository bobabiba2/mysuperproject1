import logging
from datetime import datetime
import time
import math

def logger(func):
    log = logging.getLogger(__name__)
    def wrapper(a, b, c):
        log.info("Вызов функции ", func.__name__)
        ret = func(a, b, c)
        log.info("Вызвана функция ", func.__name__)
        return ret
    return wrapper


@logger
def add(a, b, c):
   dis = b ** 2 - 4 * a * c
   print("Дискриминант D = %.2f" % dis)

   
print('>> старт')

add(2, 4, 5)

print('>> конец')