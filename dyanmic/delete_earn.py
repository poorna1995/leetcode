nums = [3,4,2]
def DeleteAndEarn(nums):
    # T=[float('-inf')]*(len(nums)+1)

    # T[0] = 0
    # T[1] = nums[0]
    # print(T)
    # T[2] =  T[i-2]+ num[i-1]-1

    #count the frequency od each number
    max_num= max(nums)
    freq =[0]*(max_num+1)
    for num in nums:
        freq[num]+=1
    # print(freq)

    #intialise the T array
    # print(max_num)
    T= [0]*(max_num+1)
    # print(T)
    T[0] = freq[0]*0
    if max_num>=1:
        T[1]=freq[1]*1
    

    #fill the Array
    for i in range(2,max_num+1):
        T[i] =max(T[i-1],T[i-2]+ freq[i]*i)
    
    return T[max_num]

print(DeleteAndEarn(nums))

        arr = [0]*(max(nums)+1)
        dp = [0]*(len(arr)+1)
        for n in nums:
            arr[n]+=n
        res = 0
        #tabulation
        for i in range(1, len(arr)):
            dp[i] = max(arr[i]+dp[i-2], dp[i-1])
        return max(dp[-1], dp[-2])