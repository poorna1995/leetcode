s='kitten'
t='sitting'

def dis(s,t,m,n):
    # base case
    if m==0 or n==0:
        return 0
    # if the last character is same 
    if s[m-1] == t[n-1]:
        cost=0
    else:
        cost =1
    
    return min(dist(s,m-1,t,n), # delettion
    dist(s,m,t,n-1), # inseration
    dist(s,m-1,t,y-1) #substition
    +cost
    )