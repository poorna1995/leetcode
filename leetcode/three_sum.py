
nums=[-1,0,1,0,-1];
class solution:
    def threeSum(self, nums):
        
        threesum= nums[2]+nums[3]+ nums[1]
        if threesum==0 :
            return True
        else:
            return False
    
print(solution().threeSum(nums))





# print(threesum)

# class solution:
#     def threeSum(self, nums,target):

