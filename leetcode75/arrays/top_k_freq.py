# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


def TopKFreq(nums, k):
    result = {}
    print(nums)
    for num in nums:
        if num not in result:
            result[num] = 0
        result[num] += 1s
    sorted_keys = [k for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True)]
    return sorted_keys[:k]



nums = [12,12,12,22,22,3]
k = 2
print(TopKFreq(nums, k))