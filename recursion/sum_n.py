def SumOfNNUmber(n):
    if n==0:
        return 0
    
    return n+SumOfNNUmber(n-1)

n=5

print(SumOfNNUmber(n))

