

def SelfProduct(nums):
    total_prod = 1
    for num in nums:
        total_prod *=num
    return [total_prod// num for num in nums]


nums = [1,2,3,4]
print(SelfProduct(nums))



def SelfProduct(nums):
    total_prod =1
    zeros = nums.count(0)
    
    if zeros>1:
        return [0]*len(nums)
    
    if zeros ==1:
        for num in nums:
            if num!=0:
                total_prod *=num
        return [total_prod if num == 0 else 0 for num in nums]
    
    for num in nums:
        total_prod *=num
    return[total_prod // num for num in nums]