def rotate(nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)   # Step 1: reverse entire array
        reverse(0, k - 1)   # Step 2: reverse first k elements
        reverse(k, n - 1)   # Step 3: reverse remaining elements

nums = [1,2,3,4,5,6,7,8]
k = 10
rotate(nums, k)
print(nums)