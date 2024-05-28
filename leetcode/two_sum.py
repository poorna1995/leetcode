# class solution:
#     def twoSum(self, nums, target):

#         for i in nums:

#             if i in hashset:
#                 return True
#             hashset.add(i)
#             return False


# target = 9
# nums = [2, 7, 11, 15]
# empytset ={}

# for i in enumerate(nums):


# )
# h = target - nums[0]
# if h in empytset:
#     print(empytset[h],i)
# preMap

# print(h)

# if h in nums:
#     print(nums[], h)


class solution:
    def twoSum(self, nums, target):
        emptyset = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in emptyset:
                return (emptyset[diff], i)
            emptyset[n] = i


nums = [2, 7, 11, 15, 10, 5]
target = 9

print(solution().twoSum(nums, target))
