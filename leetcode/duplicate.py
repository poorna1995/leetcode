number = [1, 23, 23, 52, 5, 8, 2, 5, 8, 8, 10]


# class solution:
#     def duplicateNum(self, nums):
#         # set is function that is used to store unique values and it is unordered
#         hashset = set()

#         for i in nums:
#             if i in hashset:
#                 return True
#             hashset.add(i)
#             return False


class solution:
    def duplicateNumber(self, number):
        hashset = set()
        for i in number:
            if i in hashset:
                return True
            hashset.add(i)
        return False


print(solution().duplicateNumber(number))
