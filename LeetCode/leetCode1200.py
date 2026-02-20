def minDiff(nums):
    nums.sort()
    min_diff = float("inf")
    result = []
    
    for i in range(1, len(nums)):
        min_diff = min(min_diff, nums[i]-nums[i-1])

    for i in range(1, len(nums)):
        if min_diff == nums[i] - nums[i-1]:
            result.append([nums[i-1], nums[i]])
    return result

nums = [4,1,3,1,5,9,6,3,2,7]

x = minDiff(nums)

print(x)