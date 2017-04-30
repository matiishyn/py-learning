shoppingList = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for i in shoppingList:
    if i == 'spam':
        print('ignoring ' + i)
        continue

    if i == 'bread':
        print('stopping at ' + i)
        break  # terminate loop

    print('buy ' + i)

print('==========================================================')

n = [1, 2, 3, 4, 5]
for i in n:
    if i == 10:
        break
else:
    print('this will be printer if break is never executed')