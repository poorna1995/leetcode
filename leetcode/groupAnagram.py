strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class solution:
    def groupanagrams(self, strs):
        anagram = {}
        for i in strs:
            # i is the element in the list - ["eat", "tea", "tan", "ate", "nat", "bat"]

            sortedStr = "".join(sorted(i))
            # iteration:1
            # i = "eat"
            # sorted(i) = ['a', 'e', 't']
            # "".join(sorted(i)) = "aet"

            if sortedStr not in anagram:
                # sortedStr = "aet"
                # anagram = {}
                #  anagram = {"aet": ["eat"]}

                anagram[sortedStr] = [i]
                # anagram["aet"] = ["eat"]
                #  anagram = {"aet": ["eat"], "ant" = [tan], "ant" = [nat], "abt" = [bat]}

            else:
                # anagram = {"aet": ["eat"]}
                # sortedStr = "aet"
                # i = "tea"
                # anagram = {"aet": ["eat","tea","ate"]}
                anagram[sortedStr].append(i)

        return list(anagram.values())

    #  list(anagram.values()) = [["eat","tea"],["tan","nat"],["bat"]]


# sortedStr = "".join(sorted(strs[0]))
# print(sortedStr)


# class solution:
#     def groupAnagram(self, strs):
#         anagram = {}
#         for s in strs:
#             sortedStr = "".join(sorted(s))
#             if sortedStr not in anagram:
#                 anagram[sortedStr] = [s]
#             else:
#                 anagram[sortedStr].append(s)
#         return list(anagram.values())


# print(solution().groupAnagram(strs))

# print("".join(sorted(strs[1])))

# for i in strs:
# sortedjoin = "".join(sorted(strs[i]))
# print(sortedjoin)

# anagram ={}

# print([0] * 26)

# count[ord() - ord("a")] += 1


class solution:
    def grouping(self, strs):
        anagram = {}  # create a dictionary to store the anagrams
        for i in strs:
            sortedStr = "".join(sorted(i))  # sort the first element in the list
            if sortedStr not in anagram:
                anagram[sortedStr] = [i]
            else:
                anagram(sortedStr).append(i)
        return list(anagram.values())
