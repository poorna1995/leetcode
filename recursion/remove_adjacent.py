
# def RemoveAdjacent(s):
#     if len(s) <= 1:
#         return s
    
#     stack = []  
    
#     for char in s:
#         if stack and stack[-1] == char: 
#             stack.pop()  
#         else:
#             stack.append(char) 
    
#     return ''.join(stack) 

# # Test case
# s = "abccba"
# print(RemoveAdjacent(s))


def RemoveAdjacent(s):
    if len(s)<=1:
        return s
    
    if s[0] == s[1]:
        return RemoveAdjacent(s[1:])
    else:
        return s[0] + RemoveAdjacent(s[1:])
    
# Test case
s = "abbcc"
print(RemoveAdjacent(s))