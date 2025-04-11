def SearchRotated(a, target):
    left = 0  
    right = len(a)-1
    while left <= right:
        mid = (left + right) //2 # 4
        if a[mid] == target:
            return mid
        if a[left] <= a[mid]:
            if a[left] <= target <= a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if a[mid] <= target <= a[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

    
a = [4,5,6,7,0,1,2,3]
result = SearchRotated(a,target=5)
print(result)

print(SearchRotated([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(SearchRotated([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
print(SearchRotated([1], 0))                   # Output: -1
print(SearchRotated([1, 3], 3))                # Output: 1
print(SearchRotated([5, 6, 7, 1, 2, 3, 4], 3))  # Output: 5