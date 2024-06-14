
# str = str.lower()
# y= str.isalpha()
# print(y)

# print(str)
# s= str.split()
# print(s)
# t= ''.join(s)
# print(t)
# print(t[:] == t[::-1])


# The class `solution` contains a method `isPalindrome` that checks if a given string is a palindrome
# after removing non-alphanumeric characters and converting all characters to lowercase.
# class solution:
#     def isPalindrome(self, str):
#         newstring=""

#         for c in str:
#             if c.isalnum():
#                 newstring += c.lower()
#         return newstring == newstring[::-1]

# print(solution().isPalindrome(str))


#  ord value show the value tha in the ascii value

  


# The class `solution` contains a method `ispalindrome` that checks if a given string is a palindrome
# ignoring non-alphanumeric characters and considering case-insensitivity.

class solution:
    def ispalindrome(self,str):
        l,r=0 ,len(str)-1
        while l<r:
            while l<r and not self.alphanumeric(str[l]):
                l+=1
            while l<r and not self.alphanumeric(str[r]):
                r-=1

            if str[l].lower()!= str[r].lower():
                return False
            l,r=l+1,r-1
            
        return True
    

    def alphanumeric (self,c):
    # """
    # The function checks if a character is alphanumeric (either a letter or a number) in Python.
    
    # :param c: The given code snippet defines a function named `alphanumeric` that takes a single
    # parameter `c`. The function checks if the character `c` is alphanumeric, meaning it is either a
    # letter (uppercase or lowercase) or a digit
    # """ 
        return (ord('A') <=ord(c) <= ord('Z')or
        ord('a') <=ord(c) <= ord('z')or
        ord('0') <=ord(c) <= ord('9'))


str="Was it a car or a cat I saw?"
print(solution().ispalindrome(str))
