def sumSquared(nums):
    if not nums:
        return []
    
    if nums[0]>=0:
        return [num**2 for num in nums]
    
    m = len(nums)
    for i,v in enumerate(nums):
        if v>=0:
            m=i
    
    positive_nums = nums[m:]
    negative_nums = [-1*n for n in reversed(nums[:m])]

    l = r =0 
    result = []

    while l< len(positive_nums) and r < len(negative_nums):
        if positive_nums[l] < negative_nums[r]:
            result.append(positive_nums[l])
            l+=1
        else:
            result.append(negative_nums[r])
            r+=1
    result.extend(positive_nums[l:])
    result.extend(negative_nums[r:])

    return [x*x for x in result]

nums = [-4,-1,0,3,10]
x = sumSquared(nums)
print(x)