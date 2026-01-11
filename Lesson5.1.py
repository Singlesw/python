import keyword
import string

from unicodedata import digit

var_name = input('Enter your var name: ')
var_ok = 0
var_ok += 1 if var_name[0].isdigit() else 0
var_ok += 1 if var_name in keyword.kwlist else 0
var_ok += 1 if var_name.count("_") == len(var_name) and len(var_name) > 1 else 0
for char in var_name:
    var_ok += 1 if char.isupper() else 0
    var_ok += 1 if char in string.punctuation and char != "_" else 0
var_ok = bool(not (var_ok))
print(var_ok)
