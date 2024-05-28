# write a code that array2 is a subset to the arry1


def isSubset(array1, array2, m, n):
    for i in range(m):
        for j in range(n):
            if array2[j] == array1[i]:
                break
        if j == i:
            return 1
        
array1=[11,2,6,3,0,2]
array2=[11,3,0]
m = len(array1)
n = len(array2)

if (isSubset(array1,array2,m,n)):
    print("array2[] is subset of array1[]")
else:
    print("array2[] is not subset of array1[]")
