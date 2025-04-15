def longestCommon(s,t,m,n):

    if m ==0 or n ==0:
        return 0
    
    # if the last elem of s and t matches
    if s[m-1] == t[n-1]:
        return longestCommon(s,t,m-1,n-1)+1
    
    return max(longestCommon(s,t,m-1,n),longestCommon(s,t,m,n-1) )

s= 'ABCBDAB'
t= "BDCABA"
m= len(s)
n=len(t)
print(longestCommon(s,t,m,n))
