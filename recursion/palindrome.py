def isPalindrome(string):
    if len(string)<=1 :
        return True
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False
    
print(isPalindrome("madam"))

