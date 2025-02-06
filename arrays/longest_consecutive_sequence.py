def LongestSequence(nums):
    num_set = set(nums)
    
    longest =0
    
    for n in nums:
        if n-1 not in num_set:
            length =1
            while n+length in num_set:
                length +=1
            
            longest = max(longest, length)
            
    return longest
             

    


    
nums = [100,4,200,1,3,2]
print(LongestSequence(nums))