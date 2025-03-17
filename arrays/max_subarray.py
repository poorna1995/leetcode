def MaxSubArray(a):
    current_sum =0
    max_sum = float('-inf')
    for i in range(len(a)):
        if current_sum < 0:
            current_sum = 0 
        current_sum += a[i]
        if max_sum < current_sum:
            max_sum = current_sum
    print(max_sum)
    
a = [-2,1,-3,4,-1,2,1,-5,4]
MaxSubArray(a)