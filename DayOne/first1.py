myTuple = ("One", "Two", "Three")
# print(myTuple)
# print(myTuple[1])
# print(myTuple[1:4])
# print(myTuple[1:])
# print(myTuple[:4])
# print(myTuple[-4:-1])
# print(myTuple+myTuple)

# ---- Unpack Tuples ----
(a,b,c) = myTuple
# print(a)

mySet1 = {"one","two","three","five"}
mySet = {"one","two","three"}
# for sets in mySet:
#     print(sets)

# print(mySet1)

mySet.add("four")
mySet.update(mySet1)
# print(mySet)

# # Remove from set
mySet.remove("one")
# print(mySet)

mySet.discard('two')
# print(mySet)

mySet.pop()
# print(mySet)

mySet.clear()
# print(mySet)

# ---- Dictinory ----
myDict = {
    'name':'himu',
    'age': 21,
    'gender': 'attack helicopter'
}

# print(myDict)
# print(myDict["gender"])

# myDict["City"]="Rishikesh"
# myDict["Year"]=2004
# myDict.pop('City')
# print(myDict)
# myDict.clear()
# print(myDict)

newDict = {
    "child1":{
        'name':'arman',
        'age':30,
        'country':'armenia'
    },

    "child2":{
        'name':'illa toporia',
        'age':29,
        'country':'spain, georgia'
    }
}

# print(newDict)
# print(newDict['child1']['name'])

# if (10<40):
#     print(True)
# elif (40<50):
#     print(True)
# else:
#     print(False)

class Keys:
    A = "apple"
    B = "banana"

val = "banana"

# match val:
#     case 0:
#         print("zero")
#     case Keys.A: # This works as an equality check
#         print("Found Apple")
#     case Keys.B:
#         print("Found Banana")

def function(data):
    print (f"hello {data}")
    print("hello "+data)

function("mi")

x = tuple(range(0,10))
print(x)