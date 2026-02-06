def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target-num

        if need in seen:
            return [seen[need], i]
        
        seen[num] = i


target = 9
nums = [7,2,3,6,4,5]
new = twoSum(nums, target)
print(new)