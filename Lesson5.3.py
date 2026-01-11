import string

in_string = input("Enter a string: ").title().replace(" ", "")
index = 0
hash_string = "#"
for char in in_string:
    if not (char in string.punctuation):
        hash_string += char
    index = index + 1
    if len(hash_string) >= 140: break
print(hash_string)
