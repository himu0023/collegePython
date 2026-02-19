def mountain(nums):
    count = 0 
    for i in range(1, len(nums)-1):
        if nums[i-1]<nums[i]>nums[i+1]:
            l=r=i
            while l>0 and nums[l]>nums[l-1]:
                l-=1
            while r<len(nums)-1 and nums[r]>nums[r+1]:
                r+=1
            count = max(count, r-l+1)
    return count

nums = [4,1,2,5,7,6,3,1,2]

x = mountain(nums)
print(x)