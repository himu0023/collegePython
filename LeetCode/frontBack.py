def maxSun(nums):
    nums_sum = sum(nums)
    gain = [-2*i for i in nums]

    max_sum = 0 
    total = 0
    for i in range(len(gain)):
        total += gain[i]
        if total<0:
            total = 0
    max_sum = max(max_sum, total)

    return max_sum + nums_sum
        

nums = [-1, -2, -3, 4, -5]
x = maxSun(nums)
print(x)