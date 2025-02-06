def BinarySearch(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Target found, return index
        elif nums[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found


nums = [1, 3, 5, 7, 9, 11, 13]
target = 7
index = BinarySearch(nums, target)
print(index)