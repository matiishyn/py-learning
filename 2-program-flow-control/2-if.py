name = input('''what's your name ''')
age = int(
    input('your age, {}? '.format(name))
)

if age >= 18:
    print('old enough to vote')
else:
    print('come back in {0} years'.format(18 - age))
