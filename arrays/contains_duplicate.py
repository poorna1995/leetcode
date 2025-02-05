def ContainsDuplication(nums):
    match = set()
    for n in nums:
        if n in match:
            return True
        else:
            match.add(n)
    return False
    
    

# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,4]
print(ContainsDuplication(nums))



def ContainsDuplication(nums):
    return len(set(nums))<len(nums)
