
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