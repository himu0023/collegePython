def myFun(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

numm = [1,2,4,5,4,5,2]
x = myFun(numm)
print(x)