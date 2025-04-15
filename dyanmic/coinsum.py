# def coinsum(nums,amount):
#     memo = {}
#     if amount in memo:
#         return memo[amount]
#     if amount == 0:
#         return True
#     if amount <0:
#         return False
    
#     for num in nums:
#        if(coinsum(nums,amount-num)):
#         memo[amount] =True
#         return True
#     memo[amount] = False
#     return False 


    
    # for i in range (len(nums)):
    #     for j in range(1, len(nums)):
    #         amount = amount-nums[i]
    #         print(f'i:{i} ,j:{j} and amount:{amount}')
    # return amount



# nums=[1,2,3]
# amount=4
# print(coinsum(nums,amount))


# coins=[1,2,3]
# amount=4
# def coinSum(coins,amount):
#     memo={}
#     if amount in memo:
#         return memo[amount]
#     if amount == 0:
#         return 0
#     if amount < 0:
#         return float('inf')
    
#     miniCoins = float('inf')
#     for coin in coins:
#         result= coinSum(coins, amount - coin)
#         if result!=float('inf'):
#             miniCoins = min(miniCoins,result+1 )
#         print(f'amountL:{amount}, coin:{coin}, result:{result}')
#     memo[amount] = miniCoins if miniCoins != float('inf') else -1
#     return memo[amount]





coins=[1,2,3]
amount=4
def MaxCoinSum(coins,amount):
    memo={}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('-inf')
    
    miniCoins = float('-inf')
    for coin in coins:
        result= MaxCoinSum(coins, amount - coin)
        if result!=float('-inf'):
            miniCoins = max(miniCoins,result+1 )
        print(f'amountL:{amount}, coin:{coin}, result:{result}')
    memo[amount] = miniCoins if miniCoins != float('-inf') else -1
    return memo[amount]





print(MaxCoinSum(coins,amount))