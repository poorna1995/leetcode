def tribonnaci(n):
    memo={}
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    if n in memo:
        return memo[n]
    memo[n]=tribonnaci(n-1)+tribonnaci(n-2)+tribonnaci(n-3)
    return memo[n]
    

print(tribonnaci(20))