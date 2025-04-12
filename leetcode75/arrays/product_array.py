# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
import math

# def ProductArray(nums):
#     new_prod = [1]*len(nums)
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             new_prod[i] = 0
#         new_prod[i] = math.prod(nums[:])//nums[i]

#     return new_prod
#     print(new_prod)
    

def ProductArray(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    print(result)
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    print(result)
    

    

nums = [1,2,3,4]
print(ProductArray(nums))
