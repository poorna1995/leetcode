def numsquare(n):
    T= [float('inf')]*(n+1)
    T[0] =0
    #generate the square for n
    squares=[]
    i=1
    while i*i<=n:
        squares.append(i*i)
        i+=1
    print(squares)

    # fill the array
    for i in range(1,n+1):
        for square in squares:
            if i<square:
                break
            T[i] = min(T[i],T[i-square]+1)
    return T[n]

n=12
print(numsquare(n))
