def TwoSum(nums,target):
    for i in range (len(nums)):
        print(i)
        if (target- nums[i-1]) == nums[i]:
            return  [i-1, i]
    return []
    
    
def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []


def TwoSum(nums,target):
    d ={}
    for i, num in enumerate(nums):
        t = target -num
        if t in d:
            return [d[t],i]
        else:
            d[num] =i


nums = [2,7,11,15]
target = 9
print(TwoSum(nums,target))




