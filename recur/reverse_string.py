
s = "hello"
# reverse = o+hell, ol + hel, oll+he, olle+h, olleh
# s[-1]+ s[:-1] ,s[-1]+ s[-2] + s[:-2],  s[-1]+ s[-2]+s[-3] +s[:-2]
# o 



def ReverseString(s):
    n = len(s)
    reverse = ''
    for i in range(len(s) -1,-1, -1):
        reverse+=s[i]
    return reverse
    
print(ReverseString(s))


def ReverseRecursion(s):
    n = len(s)
    if len(s) ==0:
        return ''
    return s[n-1] + ReverseRecursion(s[:n-1])
    
    
print(ReverseRecursion(s))