def twoSum(nums, target):
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement]+1, i+1]
        num_map[num] = i
    
    return []  # No solution

number = [2,3,4,5,6]
target = 9

x = twoSum(number, target)

print(x)