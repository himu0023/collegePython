# Longest mountain
def mountain(nums):
    left = 0 
    right = len(nums)-1

    while left<=right:
        if nums[left]<nums[right]:
            left+=1
        elif nums[right]<nums[left]:
            right-=1
        else:
            return nums[left]
        
nums = [0,0,0]
x = mountain(nums)
print(x)