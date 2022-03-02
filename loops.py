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

print()

for item in one_dimensional_list:
    print(item)

print()

for item in multi_dimensional_list:
    print(item)

print()

for index in range(len(one_dimensional_list)):
    print(index, end='. elem: ')
    print(one_dimensional_list[index])

print()

for row_index in range(len(multi_dimensional_list)):
    for column_index in range(len(multi_dimensional_list[row_index])):
        print('value of ' + str(row_index) + '. row, ' + str(column_index) + '. column: ', end='')
        print(multi_dimensional_list[row_index][column_index])

print()

for row_index in range(len(multi_dimensional_list)):
    for column_index in range(len(multi_dimensional_list[row_index])):
        print(multi_dimensional_list[row_index][column_index], end=' ')
    print()

print()

index = 0
while index < len(one_dimensional_list):
    print(str(index) + '. elem: ' + str(one_dimensional_list[index]))
    index = index + 1

