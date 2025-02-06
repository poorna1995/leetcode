def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []



nums = [2,7,11,15]
target = 9
print(TwoSum(nums,target))


def TwoSum(nums,target):
    match = {}
    for i,  num in enumerate(nums):
        new_val = target - num
        if new_val in match:
            return [match[new_val],i]
        else:
            match[new_val] =i
            
            




