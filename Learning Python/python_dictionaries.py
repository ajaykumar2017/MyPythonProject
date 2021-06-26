# Reference: https://appdividend.com/2021/03/25/how-to-sort-dictionary-by-value-in-python-3-7/

monthdays = {'Jan': 31, 'Feb': 28, 'Mar': 31,
             'Apr': 30, 'May': 31, 'Jun': 30,
             'Jul': 31, 'Aug': 31, 'Sep': 30,
             'Oct': 31, 'Nov': 30, 'Dec': 31}

albums = {'Flood': {1: 'Birdhouse in your Soul'}}

print('January has', monthdays['Jan'], 'days')

print('First track is', albums['Flood'][1])

# Modify existing key
monthdays['Feb'] = 29

print('February has', monthdays['Feb'], 'days')

# If we specify a different key, we would have added a new entry rather than updated the entry
monthdays['feb'] = 29

print('february has', monthdays['feb'], 'days')

# If we print we can see that a new element is added in 13th position
print(monthdays)

# del function is used to delete a key in dictionary
del monthdays['feb']

print(monthdays)

# Dictionaries have no order - like lists, the indexes(keys) must be unique - but there is a
# no logical order to the keys in the dictionary
months = monthdays.keys()
print(months)
# o/p ->   dict_keys(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# The len function returns the number of elements, the key/value pairs, stored ina a dictionary
print(len(monthdays))

# sorting dictionaries
# months = monthdays.keys()
# months.sort()
# print(months)

months = monthdays.items()
# Sort Dictionary By Value in Python
sorted_by_val = {keys: values for keys, values in sorted(
    monthdays.items(), key=lambda element: element[1])}
print(sorted_by_val)

# To sort it in descending order, add reverse=True.
sorted_by_val = {keys: values for keys, values in sorted(
    monthdays.items(), key=lambda element: element[1], reverse=True)}
print(sorted_by_val)

# Iterating through the dictionaries
for keys in sorted_by_val:
    print('There are', keys, 'days in', monthdays[keys])

# Sort Dictionary by value using a for loop
sorted_values = sorted(monthdays.values())  # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in monthdays.keys():
        if monthdays[k] == i:
            sorted_dict[k] = monthdays[k]
            break

print(sorted_dict)

# Before Python 3.7, Sort Dictionary by values using the sorted()
import operator
from collections import OrderedDict

data = {1: 21, 3: 46, 4: 31, 2: 19, 0: 11}

sorted_tuples = sorted(data.items(), key=operator.itemgetter(1))
sorted_dict = OrderedDict()

for k, v in sorted_tuples:
    sorted_dict[k] = v

print(sorted_dict)
