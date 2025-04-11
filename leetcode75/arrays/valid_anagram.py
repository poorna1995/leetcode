# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# def ValidAnagram(s,t):
#     if len(s) != len(t):
#         return False
#     if sorted(s) == sorted(t):
#         return True
#     return False
        

# def ValidAnagram(s,t):
#     if len(s)!=len(t):
#         return False
#     count = {}
#     for i in range(len(s)):
#         count[s[i]] = count.get(s[i], 0) + 1
#         count[t[i]] = count.get(t[i], 0) - 1
#     for value in count.values():
#         if value != 0:
#             return False
#     return True
    
    




# def ValidAnagram(s,t):
#     Counter(s) == Counter(t)
    
    


def ValidAnagram(s,t):
    if len(s)!=len(t):
        return False
    CountS, CountT = {}, {}
    
    for i in range(len(s)):
        CountS[s[i]] = CountS.get(s[i], 0) + 1
        CountT[t[i]] = CountT.get(t[i], 0) + 1
    return CountS == CountT

# s = "anagram"
# t = "nagaram" 
  
s = "rat" 
t = "car" 
        
print(ValidAnagram(s,t))