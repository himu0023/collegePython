nums = [4,3,2,7,8,2,3,1]

seen = set(nums)
result = []
for i in range(1, len(nums)+1):
    if i not in seen:
        result.append(i)

print(result)