# [12, 3, 4, 10] => [10, 12, 3, 4]
test_array = [12, 3, 4, 10]
print(f'test array: {test_array}')
if len(test_array) > 1:
    test_array.insert(0, test_array.pop())
print(f'test array moved: {test_array}')

# [1] => [1]
test_array = [1]
print(f'test array: {test_array}')
if len(test_array) > 1:
    test_array.insert(0, test_array.pop())
print(f'test array moved: {test_array}')

# [] => []
test_array = []
print(f'test array: {test_array}')
if len(test_array) > 1:
    test_array.insert(0, test_array.pop())
print(f'test array moved: {test_array}')

# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
test_array = [12, 3, 4, 10, 8]
print(f'test array: {test_array}')
if len(test_array) > 1:
    test_array.insert(0, test_array.pop())
print(f'test array moved: {test_array}')
