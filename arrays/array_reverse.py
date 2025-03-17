def ReverseArray(a):
    reverse =[]
    for i in range(len(a)-1,-1,-1):
        reverse.append(a[i])
        print(i)
    
    print(reverse)
# Time complexity: O(N), where N is the number of elements in the array.
# Auxiliary Space: O(N), as we are using an extra array to store the reversed elements.  
a= [1, 4, 3, 2, 6, 5]
ReverseArray(a)


def ReverseTwoPointer(a):
    left , right = 0, len(a)-1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    print(a)

ReverseTwoPointer(a)
# Time complexity: O(N), where N is the number of elements in the array.
# Auxiliary Space: O(1), as we are not using any extra space.W