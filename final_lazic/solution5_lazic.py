roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50}

keys1 = []
values1 = []
items1 = []

for item in roman_numerals.keys():
    keys1.append(item)
print('Keys: ' + ', '.join(keys1))

for item in roman_numerals.values():
    values1.append(item)
print('Values: ' + str(values1))

for item in roman_numerals.items():
    items1.append(item)
print('Items: ' + str(items1))
