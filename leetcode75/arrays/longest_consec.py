# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3


# [0,3,7,2,5,8,4,6,0,1]



# def LongestConsecutive(nums):
#     result = []
#     nums.sort()
#     for i in range(len(nums)):
#         if nums[i-1]+1 == nums[i]:
#             result.append(nums[i])
#         else:
#             i += 1
#     return len(result)
            
        
    
#     print(nums)
    
    
    
    
def LongestConsecutive(nums):
    num_set = set(nums)
    print(num_set)
    longest = 0
    for num in num_set:
        if num -1 not in num_set: # this is the starting sequence
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num +=1
                current_streak +=1
        longest = max(longest, current_streak)
    return longest
                
    
        
    
    
nums  = [1,0,1,2]
print(LongestConsecutive(nums))
