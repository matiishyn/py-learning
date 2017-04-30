for i in range(1, 20):  # [1,20)
    print('i is now {}'.format(i))
print('==========================================================')

number = '1,022,156,245'
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
print()
print('==========================================================')

number = '1,022,156,245'
filteredNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        filteredNumber = filteredNumber + number[i]
print()
print('filtered {}'.format(filteredNumber))
print('==========================================================')

number = '1,022,156,245'
filteredNumber = ''
for char in number:
    if char in '0123456789':
        filteredNumber = filteredNumber + char
print('chars {}'.format(filteredNumber))
print('==========================================================')

for el in ['one', 'two', 'three', 'four']:
    print('el: ' + el)
    # print('el: {}'.format(el))

print('==========================================================')

for i in range(0, 20, 5):  # range step
    print(i)
print('==========================================================')

for i in range(1, 11):
    for j in range(1, 11):
        print('{:4}'.format(i * j), end='')
    print()
