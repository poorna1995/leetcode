
# Time Complexity: O(N)
# Auxiliary Space: O(1)
def MaxMin(a):
    max = float('-inf')
    min = float('inf')
    for i in a:
        if i > max:
            max = i
        if i < min:
            min = i
    print(f"maximum number = {max},\nminimum number = {min}" )
    print(a)
    
a = [22, 14, 8, 17, 35, 3]
MaxMin(a)
    
    

# Sorting

def SortMaxMin(a):
    a.sort()
    print(f"maximum number = {a[-1]},\nminimum number = {a[0]}" )
    print(a)

# Time complexity: O(n log n), where n is the number of elements in the array, as we are using a sorting algorithm.
# Auxilary Space: is O(1), as we are not using any extra space.