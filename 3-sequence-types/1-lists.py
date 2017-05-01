# ipAddress = input('IP: ')
ipAddress = '192.02.244.225'
print(ipAddress.count('.'))
print('=======================================================')

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

odd.append(9)                       # append

numbers = odd + even
numbers2 = numbers

numbers.sort()                      # sort existing list, NOT return new list
sortedNumbers = sorted(numbers2)    # sorting that returns a list

print(numbers)
print(numbers2)

if numbers == sortedNumbers:        # TRUE
    print('Lists are equal')
