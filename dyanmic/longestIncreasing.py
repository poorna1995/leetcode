array = [ 0,3,1,6,2,2,7]


def longestSub(array):
    LIS= [1]* len(array)
    for i in range(len(array)-1,-1,-1):
        for j in range (i+1,len(array)):
            if array[i] <array [j]:
                LIS[i] = max(LIS[i]+1,LIS[j])
        return max(LIS)

print( longestSub(array))