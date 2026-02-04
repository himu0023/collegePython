year = int(input("Enter year to check its leap or not: "))

if year%400==0:
    print(year, "is leap")
elif year%100==0:
    print(year, "is not leap")
elif year%4==0:
    print(year, "is leap")
else:
    print(year, "is not leap")