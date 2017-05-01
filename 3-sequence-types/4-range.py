l = range(10)
print(list(l))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('=' * 50)
# ===============================================================

s = 'abcdefghijklmnopqrstuvwxyz'
print(s.index('e'))
print(s[4])
print()

r = range(1, 100, 2)
print(r.index(7))
print(r[3])
print(7 in r)  # True - check if exists in range

print('=' * 50)
# ===============================================================

r1 = range(1, 10)
r2 = r1[::2]
print(r2)

print('=' * 50)
# ===============================================================

decimals = range(0, 100)
r1 = decimals[3:40:3]
r2 = range(3, 40, 3)
print(r1 == r2)  # True - equals

print('=' * 50)
# ===============================================================

r1 = range(0, 5, 2)  # [0, 2, 4]
r2 = range(0, 6, 2)  # [0, 2, 4]
print(r1 == r2)  # True - equals

print('=' * 50)

r = range(1, 10)
for i in r[::-2]:
    print(i)  # 9 7 5 3 1

print()
# SAME AS

for i in range(9, 0, -2):
    print(i)  # 9 7 5 3 1

print()

print(range(1, 10)[::-2] == range(9, 0, -2))  # True

print('=' * 50)
# ===============================================================

backStr = 'nohtyP'
print(backStr[::-1])  # printed backward


r = range(0, 10)
for i in r[::-1]:
    print(i)  # 9 8 7 6 5 4 3 2 1 0
