import string

letters = input('Enter your letters: ')
out_string = string.ascii_letters[
    string.ascii_letters.find(letters[0]):
    string.ascii_letters.find(letters[2]) + 1]
print(f'Out string {out_string}')
