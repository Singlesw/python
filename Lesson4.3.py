import random

array = []
count = random.randint(3, 10)
for i in range(count):
    array.append(random.randint(1, 100))
print(f'In array  {array}')
out_array = [array[0]] + [array[2]] + [array[-2]]
print(f'Out array {out_array}')
