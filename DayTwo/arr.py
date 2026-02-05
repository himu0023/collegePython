arrOne = ['one', 'two', 'three', 'four']
print(arrOne[0])
print(len(arrOne))
arrOne.append('five')
print(arrOne)
arrOne.pop()
arrOne.remove('one')

print(arrOne)

myTuple = ('one', 'two', 'three')
myVal = iter(myTuple)

print(next(myVal))
print(next(myVal))
print(next(myVal))

for i in myTuple:
    print(i)