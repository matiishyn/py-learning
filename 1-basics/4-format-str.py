age = 25
print('My age is ' + str(age) + ' years')

# replacement filed
print('My age is {0} years'.format(age))
print('There are {0} days in {1}, {2}'.format(31, 'Jan', 'Mar'))

# reusing data
print('''Jan:{2}, Feb:{0}, Mar:{2}, Apr:{1}'''.format(28, 30, 31))
print()

print('My age is %d years' % age)
print('My age is %d %s, %d %s' % (age, 'years', 6, 'month'))
print()

# formatting
for i in range(1, 12):
    print('%2d squared is %4d, cubed is %4d' % (i, i ** 2, i ** 3))
print()

# formatting
for i in range(1, 12):
    print('{0:2} squared is {1:4}, cubed is {2:<4}'.format(i, i ** 2, i ** 3))
print()

print('PI is approx %12f' % (22 / 7))
print('PI is approx %12.50f' % (22 / 7))
print('PI is approx {0:12.50f}'.format(22 / 7))
print()

# auto assignment
print('auto {} setting with formatting {:4}'.format(1, 2))
