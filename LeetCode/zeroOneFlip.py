def maxOne(nums):
    current_sum = 0 
    max_gain = 0 
    orig_sum = sum(nums)

    for x in nums:
        if x == 0:
            gain = 1
        else:
            gain = -1
        
        current_sum = max(gain, current_sum+gain)
        max_gain = max(current_sum, max_gain)

    return max_gain + orig_sum

nums = [1,1,1,1,0,0,0,0,0,1,0,1,0]
x = maxOne(nums)
print(x)