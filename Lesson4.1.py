# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
array = [0, 1, 0, 12, 3]
print(f'In array  {array}')
i = len(array) - 1
while i >= 0:
    if array[i] == 0:
        array.append(array.pop(i))
    i -= 1
print(f'Out array {array}')

# [0] -> [0]
array = [0]
print(f'In array  {array}')
i = len(array) - 1
while i >= 0:
    if array[i] == 0:
        array.append(array.pop(i))
    i -= 1
print(f'Out array {array}')

# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
array = [1, 0, 13, 0, 0, 0, 5]
print(f'In array  {array}')
i = len(array) - 1
while i >= 0:
    if array[i] == 0:
        array.append(array.pop(i))
    i -= 1
print(f'Out array {array}')

# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
array = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print(f'In array  {array}')
i = len(array) - 1
while i >= 0:
    if array[i] == 0:
        array.append(array.pop(i))
    i -= 1
print(f'Out array {array}')
