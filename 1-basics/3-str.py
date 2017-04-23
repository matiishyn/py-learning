p = "Norwegian Blue"
print(p)
print(p[3])             # 0,1,2,3 char
print(p[0])             # first char
print(p[-1])            # last char
print(p[0:6])           # start at 0, 6 chars
print(p[:6])            # start at 0, 6 chars
print(p[6:])            # start at 6, till the end
print(p[-4:2])          # not correct
print(p[-4:-2])         #
print()
print(p[0:6:2])         # start at 0, end at 6, step 2
print(p[0:6:3])         # start at 0, end at 6, step/skip 3
print()

n = '9,223,432,346,123'
print(n[1::4])          # print commas

n = '1,2,3,4,5,6,7'
print(n[::2])           # print numbers
print()

print('print' 'without' 'plus')
a = 'print cannot be done'
b = 'without plus'
print(a + b)
print()

print('Hello ' * 5)
print('Hello ' * (5 + 4))
print('Hello ' * 5 + '4')
print()

today = 'friday'
print('day' in today)
