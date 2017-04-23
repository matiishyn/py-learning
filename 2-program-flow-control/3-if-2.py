age = 66  # int(input('how old are u? '))

# if (age >= 18) and (age <= 65):
if 18 <= age <= 65:
    print('good to work')
print()

if (age < 18) or (age > 65):
    print('enjoy free time')
else:
    print('work')

print()
print('''FALSY values:
    False: {0},
    None: {1},
    0: {2},
    0.0: {3},
    empty list []: {4},
    empty tuple (): {5},
    empty string '': {6},
    empty string "": {7},
    empty mapping {{}}: {8},
'''.format(
    False,
    bool(None),
    bool(0),
    bool(0.0),
    bool([]),
    bool(()),
    bool(''),
    bool(""),
    bool({}),
))

print(not False)
print(not True)
