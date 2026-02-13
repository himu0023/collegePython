def median(nums1, nums2):
    # Merge and sort
    merged = nums1 + nums2
    merged.sort()
    
    n = len(merged)
    mid = n // 2
    
    # If even length
    if n % 2 == 0:
        return (merged[mid-1] + merged[mid]) / 2.0
    # If odd length
    else:
        return float(merged[mid])

# Test
nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6]

result = median(nums1, nums2)
print(f"Median = {result}")  # Median = 3.5