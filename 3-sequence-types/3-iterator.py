s = '123456789'

myIterator = iter(s)

print(myIterator)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

print('==================================================')

for char in s:
    print(char)
print()
# exactly the same
for char in iter(s):
    print(char)
