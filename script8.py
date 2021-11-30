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