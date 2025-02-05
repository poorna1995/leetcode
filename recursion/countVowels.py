# count Vowels

def isVowel(char):
    char = char.lower()
    if char in "aeiou":
        return True
    else:
        return False
    

def CountVowels(string):
    count = 0
    for c in string:
        if isVowel(c):
            count+=1
    return count
    
    

result = CountVowels("PoornaPraneesha")
print(result)



def RecursiveCountVowels(string):
    if len(string) == 0:
        return 0
    print(string)
    return (1 if isVowel(string[0]) else 0) + RecursiveCountVowels(string[1:])


output = RecursiveCountVowels("PoornaPraneesha")
print(output)