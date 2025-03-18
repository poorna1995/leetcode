# def ChocolateDistribution(a, m):
#     n = len(a)
#     a.sort()
#     minimum = float('inf')
#     for i in range(n-m+1):
#         diff = a[i+m-1] -a[i]
#         if diff < minimum:
#             minimum = diff
#     print(minimum)
#     return minimum

def ChocolateDistribution(a, m):
    n = len(a)
    a.sort() 

    minimum = float('inf')

    for i in range(n - m + 1):

        diff = a[i + m - 1] - a[i]
        if diff < minimum:
            minimum = diff
    return minimum

a = [7, 3, 2, 4, 9, 12, 56]
m = 3

result = ChocolateDistribution(a,m)
print(result) # Expected output: 2