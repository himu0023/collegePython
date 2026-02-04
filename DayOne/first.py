name = "   Hello World   "

# print(name)
# name = name.strip()
# print(name[0:5])
# print(name[2:])
# print(name[3:8])
# print(name[:-1])
# print(name.upper())
# print(name.lower())

# print(100==(10*10))

myList = ['one', 'two', 'three', 'four']

print(myList[1])
print(myList[2:4])
print(myList[::-1])


# 2. Replace element at index 1
myList[1] = 'Mango'
print("After myList[1] = 'Mango':", myList)

# 3. Slice assignment
myList[1:3] = ['india', 'bhutan', 'tibet']
print("After slice assignment:", myList)

# 4. Append correctly (don't reassign!)
myList.append("Fuckk off")
print("After append:", myList)

# 5. Create a copy
myVal = myList.copy()
print("Copy (myVal):", myVal)

# 6. Remove from copy (but careful: 'Fuck off' vs 'Fuckk off')
# Note: 'Fuck off' doesn't exist, 'Fuckk off' does
myVal.remove("Fuckk off")  # This modifies myVal in place, returns None
print("After remove (myVal):", myVal)