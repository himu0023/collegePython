def containDuplicate(nums,k):
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen)>k:
            seen.remove(num[i-k])
    return False

arr = [1,2,3,1]
a = 3
b = containDuplicate(arr, a)
print(b)