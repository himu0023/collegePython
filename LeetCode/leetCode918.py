nums = [2,3,6,4]
arr = nums[::-1]
arr.remove(arr[0])
# new_nums = nums + reversed(nums)
# print(new_nums)
new_arr = nums+arr
print(nums)
print(arr)
print(new_arr)
total = 0 
max_sum = float("-inf")

for i in range(len(new_arr)):
    if new_arr[i]>new_arr[i+1] and new_arr[i]<0:
        total = new_arr[i]
    total += new_arr[i]
    max_sum = max(total, max_sum)
print(max_sum)