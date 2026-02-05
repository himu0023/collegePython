a = 10
b = 0
try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
finally:
    print("This will always execute. No matter what.")