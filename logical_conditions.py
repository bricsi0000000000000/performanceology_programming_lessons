a = True
b = False
c = a == b
d = a != b
e = 1 == 1
f = 1 == '1'

print(a)
print(b)
print('a == b: ', end='')
print(c)
print('a != b: ', end='')
print(d)
print('1 == 1: ', end='')
print(e)
print('1 == "1": ', end='')
print(f)

print()

g = a and b
h = a or b

print('a and b: ', end='')
print(g)
print('a or b: ', end='')
print(h)
