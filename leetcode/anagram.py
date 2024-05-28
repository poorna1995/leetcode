# class solution:
#     def isAnagram(self, s, t):
#         # return sorted(s) == sorted(t)
#         # return Counter(s) == Counter(t)
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}
#         # countS = {} is the empty dictionary
#         # countT = {} is the empty dictionary
#         for i in range(len(s)):
#             countS[s[i]] = countS.get(s[i], 0) + 1
#             countT[t[i]] = countT.get(t[i], 0) + 1
#         return countS == countT


# s = "anagram"
# t = "nag"
# print(solution().isAnagram(s, t))


s = "put"
t = "but"


class solution:
    def IsAnagram(self, s: str, t: str):
        CountS, CountT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            CountS[s[i]] = CountS.get(s[i], 0) + 1
            CountT[t[i]] = CountT.get(t[i], 0) + 1
        return CountS == CountT


print(solution().IsAnagram(s, t))
