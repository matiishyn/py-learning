l1 = []
l2 = list()

if l1 == l2:  # TRUE
    print('{} and {} are equal'.format(l1, l2))

print(list('a list'))
print('==============================================')

list1 = [1, 2, 3, 4, 5]
list2 = list1

list2.sort(reverse=True)
print(list1)
print(list2)
print(list1 == list1)  # TRUE - both lists are changed
