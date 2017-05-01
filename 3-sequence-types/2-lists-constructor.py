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
print(list1 == list2)  # TRUE - both lists are changed
print(list1 is list2)  # TRUE - both lists are the same

list3 = list(list1)
print(list1 == list3)  # TRUE - they are equals
print(list1 is list3)  # FALSE - but they are not the same
print('==============================================')

