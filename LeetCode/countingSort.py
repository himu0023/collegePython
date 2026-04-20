def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)

    # Creating a count array 
    count = [0]*(max_val+1)

    # Store frequency of each element
    for num in arr:
        count[num]+=1

    # Sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i])
    
    return sorted_arr

arr = [1,5,3,2,6,7,4,9,1,1,0]
print(counting_sort(arr))