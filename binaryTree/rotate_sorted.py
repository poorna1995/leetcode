def FindMin(nums):
    left,right = 0, len(nums)-1
    while left <right:
        mid = left + (right-left)//2
        
        if nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid+1
    return nums[left]
        
        

nums = [3,4,5,1,2]
print(FindMin(nums))
