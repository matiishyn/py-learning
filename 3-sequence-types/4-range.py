l = range(10)
print(list(l))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('==============================================')

s = 'abcdefghijklmnopqrstuvwxyz'
print(s.index('e'))
print(s[4])
print()

r = range(1, 100, 2)
print(r.index(7))
print(r[3])
print(7 in r)  # True - check if exists in range
print('==============================================')

r1 = range(1, 10)
r2 = r1[::2]
print(r2)
print('==============================================')

decimals = range(0, 100)
r1 = decimals[3:40:3]
r2 = range(3, 40, 3)
print(r1 == r2)  # True - equals
