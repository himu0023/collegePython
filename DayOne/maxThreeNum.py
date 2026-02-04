a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if b>a:
    if b>c:
        print(b, "is greater.")
    else:
        print(c, "is greater.")
elif c> a: 
    print(c, "is greater.")
else:
    print(a, "is greater.")