character = 'a'
text = 'minden'
number = 4
floating_number = 4.6

print('karakter:', end='')
print(character)

print('szöveg:', end='')
print(text)

print('szám:', end='')
print(number)

print('tizedes:', end='')
print(floating_number)

# üres sor
print()

n1 = '1'
n2 = 1

print('n1 tipusa: ', end='')
print(type(n1))
print('n2 tipusa: ', end='')
print(type(n2))

print()

n3 = int(n1)
print('n3 értéke: ', end='')
print(n3)
print('n3 tipusa: ', end='')
print(type(n3))

print()

n4 = str(n2)
print('n4 értéke: ', end='')
print(n4)
print('n4 tipusa: ', end='')
print(type(n4))

print()
print('-----------------')

n1 = '3.14'
n2 = 3.14


print('n1 tipusa: ', end='')
print(type(n1))
print('n2 tipusa: ', end='')
print(type(n2))

print()

n3 = float(n1)
print('n3 értéke: ', end='')
print(n3)
print('n3 tipusa: ', end='')
print(type(n3))

print()

n4 = str(n2)
print('n4 értéke: ', end='')
print(n4)
print('n4 tipusa: ', end='')
print(type(n4))

print()

one_dimensional_list = [0, 1, 2, 3, 4, 5, 6]
multi_dimensional_list = [['a', 'b', 'c'],['d', 'e', 'f']]

print('lista: ', end='')
print(one_dimensional_list)

print('lista 2. eleme: ', end='')
print(one_dimensional_list[1])

print('több dimenziós lista: ', end='')
print(multi_dimensional_list)

print('több dimenziós lista 1. dimenziója: ', end='')
print(multi_dimensional_list[0])

print('több dimenziós lista 1. dimenziójának 2. eleme: ', end='')
print(multi_dimensional_list[0][1])

print('lista hossza: ', end='')
print(len(one_dimensional_list))
