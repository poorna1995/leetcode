s = 'poornapraneesha'

def CountVowels(s):
    count =0
    vowels='aeiou'
    for str in s:
        if str in vowels:
            count+=1
        else:
            continue
    return count



print(CountVowels(s))


print(s[:-1])

def CountRecursionVowels(s):
    vowels = 'aeiouAEIOU'
    if len(s) == 0:
        return 0
    if s[-1] in vowels:
        return 1 + CountRecursionVowels(s[:-1])
    else:
        return CountRecursionVowels(s[:-1])


print(CountRecursionVowels(s))