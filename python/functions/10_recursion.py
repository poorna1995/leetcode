def recursion(num):
    if num ==0:
        return 1
    else:
        num=num*recursion(num-1)
        return num

print(recursion(5))
    

