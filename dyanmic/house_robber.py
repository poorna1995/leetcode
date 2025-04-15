def houseRobber(nums,i=0,memo=None):
    if memo is None:
        memo = {}
    if i in memo :
        return memo[i]
    if i>=len(nums):
        return 0
    if len(nums) ==0:
        return 0
    
    include = nums[i] + houseRobber( nums,i+2,memo)
    exclude = houseRobber( nums, i+1, memo)

    memo[i] = max(include,exclude)
    return memo[i]


nums = [2,1,3,1,4,6,2]
print(houseRobber(nums,i=0,memo=None))
