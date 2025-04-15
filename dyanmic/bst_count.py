n=4



def bstcount(n):
    T = [0] * (n + 1)
    T[0] = 1
    T[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            T[i] += T[j] * T[i - 1 - j]
    return T[n]

print(bstcount(3))

