def ValidAnagram(s,t):
    if len(s)!=len(t):
        return False
    for char in set(s):
        if s.count(char) != t.count(char):
            return False
    return True

s = "anagram" 
t = "nagaram"
print(ValidAnagram(s,t))

