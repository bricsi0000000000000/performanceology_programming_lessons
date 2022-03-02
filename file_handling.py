import matplotlib.pyplot as plt
import numpy as np

def convertItemsToNumber(list):
    new_list = []
    for index in range(len(list)):
        if list[index] != '':
            new_list.append(float(list[index]))
    return new_list

def multiplyListByNumber(list, n):
    for index in range(len(list)):
        list[index] = list[index] * n

file = open('gas.txt').read()
data = file.split(';')
print(data)

new_list = convertItemsToNumber(data)
print(new_list)
multiplyListByNumber(new_list, 3.14)
print(new_list)

plt.plot(data)
plt.show()

"""
file = open('ACC.csv')
content = file.read()
rows = content.split('\n')

columns = [[]]

for index in range(1, len(rows)):
    columns.append([])
    values = rows[index].split(';')
    for value in values:
        columns[index].append(value)

for row in range(len(columns)):
    for col in range(len(columns[row])):
        print(columns[row][col], end='; ')
    print()

"""
