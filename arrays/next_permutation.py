from itertools import permutations
def NextPermutation(a):
    n = len(a)
    
    a[n-1], a[n-2] = a[n-2], a[n-1]
    
    return a
    

a = [1,2,3]
print(NextPermutation(a))