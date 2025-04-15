# cost=[10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]


def miniCost(cost):
    n = len(cost)
    if n==0:
        return 0
    if n==1:
        return cost[0]
    T = [0]*n
    T[0]=cost[0]
    T[1]=cost[1]
    for i in range(2,n):
        T[i] = min(T[i-1]+cost[i],T[i-2]+cost[i])
        print(T)
    return min(T[n-1],T[n-2])

print(miniCost(cost))

