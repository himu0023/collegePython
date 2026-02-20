def Duplicate(arr, k):
    seen = set()
    for i,num in enumerate(arr):
        if num in seen:
            return True 
        seen.add(num)
        if len(seen)>k:
            seen.remove(arr[i-k])
    return False

nums = [1,2,3,4,1]
k = 3

x = Duplicate(nums, k)

print(x)