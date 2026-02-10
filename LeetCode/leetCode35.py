def searchInerst(nums, target):
    
    low = 0 
    high = len(nums)-1

    while low <= high:

        mid = low+(high-low)//2
        
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return low

nums = [1,2,4,5,6]
target = 3

x = searchInerst(nums, target)
print(x)