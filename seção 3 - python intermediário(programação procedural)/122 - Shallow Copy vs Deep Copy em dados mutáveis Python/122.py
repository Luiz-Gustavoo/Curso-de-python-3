import copy

# copy

d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': [0, 1 ,2],
}
# d2 = copy.copy(d1)
#d2 = d1.copy()
# d2 = d1

# deep copy
d2 = copy.deepcopy(d1)

d2['a'] = 4
d2['d'][2] = 100
print(d2)
print(d1)


