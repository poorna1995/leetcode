n=2

def divisorGame(n):
    if n==1 :
        return False
    
    elif n%2 == 0 :
        return True
    else :
        return False


print(divisorGame(2))
