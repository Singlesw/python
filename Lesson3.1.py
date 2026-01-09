num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
function = input("Enter a function: ")
if function == "+":
    result = num1 + num2
elif function == "-":
    result = num1 - num2
elif function == "*":
    result = num1 * num2
elif function == "/" and num2 != 0:
    result = num1 / num2
else:
    result = None
print(f'The result is {result}')
