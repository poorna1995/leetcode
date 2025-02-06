# def TopKFrequent(nums, k):
#     dic ={}
#     for num in set(nums):
#         dic[num] = nums.count(num)
    
#     sorted_dic = dict(sorted(dic.items(),key=lambda item: item[1],reverse = True))
#     new= list(sorted_dic.keys())
#     return new[:k]
#         # print(nums.count(num))
        
    
    
    
from collections import Counter
def TopKFrequent(nums, k):
    counts = dict(Counter(nums))
    print(counts.get)
    sorted_keys = sorted(counts, key=counts.get, reverse=True)  # Sort by frequency
    print(sorted_keys)
    return sorted_keys[:k] 

    

nums = [5,5,5,2,2,3]
k = 2
print(TopKFrequent(nums, k))


# def TopKFrequent(nums,k):
#     dic ={}
#     counts = Counter(nums)
#     sorted_val = sorted(counts, key=counts.get, reverse=True)
#     return sorted_val[:k]
        