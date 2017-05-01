i = 0
while i < 10:
    print(i)
    i += 1

print('============================================')

correctNumbers = ['1', '3', '5', '7', '9']
chosen = ''
while chosen not in correctNumbers:
    chosen = input('odd number 0-10? ')
    if chosen == 'exit':
        print('Game over :(')
        break
else:
    print('{} is a correct odd number'.format(chosen))
