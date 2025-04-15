s="11106"

def decode(s):
    if not s or s[0]=='0':
        return 0
    n=len(s)
    T = [0]*(n+1)
    T[0] = 1
    T[1] = 1
    for i in range(2,n+1):
        if s[i-1]!=0:
            T[i] = T[i]+T[i-1]
        
        two_digit = int(s[i-2:i])
        print(f'two_digit:{two_digit}')
        if 10<=two_digit<=26:
            T[i]=T[i]+T[i-2]
    return T[n]

    # print(T)

    # for i in range(2, n + 1):
    #     # Single character decoding
    #     if s[i - 1] != '0':
    #         T[i] += T[i - 1]
        
    #     # Two character decoding
    #     two_digit = int(s[i - 2:i])
    #     if 10 <= two_digit <= 26:
    #         T[i] += T[i - 2]
    
    # return T[n]  
        




print(decode(s))
