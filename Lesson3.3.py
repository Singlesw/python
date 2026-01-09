# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
test_array = [1, 2, 3, 4, 5, 6]
print(f'Input array: {test_array}')
array_mid = len(test_array) - len(test_array) // 2
result_array = [test_array[:array_mid]] + [test_array[array_mid:]]
print(f'Result array: {result_array}')

# [1, 2, 3] => [[1, 2], [3]]
test_array = [1, 2, 3]
print(f'Input array: {test_array}')
array_mid = len(test_array) - len(test_array) // 2
result_array = [test_array[:array_mid]] + [test_array[array_mid:]]
print(f'Result array: {result_array}')

# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
test_array = [1, 2, 3, 4, 5]
print(f'Input array: {test_array}')
array_mid = len(test_array) - len(test_array) // 2
result_array = [test_array[:array_mid]] + [test_array[array_mid:]]
print(f'Result array: {result_array}')

# [1] => [[1], []]
test_array = [1]
print(f'Input array: {test_array}')
array_mid = len(test_array) - len(test_array) // 2
result_array = [test_array[:array_mid]] + [test_array[array_mid:]]
print(f'Result array: {result_array}')

# [] => [[], []]
test_array = []
print(f'Input array: {test_array}')
array_mid = len(test_array) - len(test_array) // 2
result_array = [test_array[:array_mid]] + [test_array[array_mid:]]
print(f'Result array: {result_array}')
