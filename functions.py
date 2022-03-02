numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def printNumbers():
    for item in numbers:
        print(item, end=', ')

def printList(list):
    for item in list:
        print(item, end=', ')

def multiplyListByNumber(n):
    for index in range(len(numbers)):
        numbers[index] = numbers[index] * n

def roundUpToTwoDecimals():
    for index in range(len(numbers)):
        numbers[index] = round(numbers[index], 2)

def convertItemsToNumber(list):
    new_list = []
    for index in range(len(list)):
        if list[index] != '':
            new_list.append(int(list[index]))
    return new_list

printNumbers()
multiplyListByNumber(3)

print()

printNumbers()
multiplyListByNumber(1.1)

print()

printNumbers()

print()

roundUpToTwoDecimals()
printNumbers()


print()
print()

string_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(type(string_numbers[0]))
printList(string_numbers)

print()

converted_list = convertItemsToNumber(string_numbers)
print(type(converted_list[0]))
printList(converted_list)