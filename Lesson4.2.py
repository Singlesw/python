# [0, 1, 7, 2, 4, 8] = > (0 + 7 + 4) * 8 = 88
array = [0, 1, 7, 2, 4, 8]
print(f'In array  {array}')
index = 0
total = 0
while index < len(array):
    total += 0 if index % 2 else array[index]
    index += 1
total = total * array[-1] if array else 0
print(f'Result: {total}')

# [1, 3, 5] = > 30
array = [1, 3, 5]
print(f'In array  {array}')
index = 0
total = 0
while index < len(array):
    total += 0 if index % 2 else array[index]
    index += 1
total = total * array[-1] if array else 0
print(f'Result: {total}')

# [6] = > 36
array = [6]
print(f'In array  {array}')
index = 0
total = 0
while index < len(array):
    total += 0 if index % 2 else array[index]
    index += 1
total = total * array[-1] if array else 0
print(f'Result: {total}')

# [] = > 0
array = []
print(f'In array  {array}')
index = 0
total = 0
while index < len(array):
    total += 0 if index % 2 else array[index]
    index += 1
total = total * array[-1] if array else 0
print(f'Result: {total}')
