import math

nums = [-4,-1,0,3,1,0]
m=0
for i,n in enumerate(nums):
    if n>=0:
        m=i
        break
positive_num = nums[m:]
negative_num = [-1*n for n in reversed(nums[:m])]
print(positive_num)
print(negative_num)