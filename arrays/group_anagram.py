def GroupAnagram(strs):
    match ={}
    for s in strs:
        sorted_key = ''.join(sorted(s)) 
        if sorted_key in match:
            match[sorted_key].append(s)
        else:
            match[sorted_key] =[s]
    return list(match.values())
            
        

strs = ["eat","tea","tan","ate","nat","bat"]

print(GroupAnagram(strs))


# def GroupAnagram(strs):
#     match ={}
#     for s in str:
#         sorted_val = "".join(sorted(s))
#         if sorted_key in match:
#             match[sorted_key].append(s)
#         else:
#             match[sorted_key] = [s]
#     return (list(match.values()))
            
            