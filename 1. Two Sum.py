#첫시도
class Solution(object):
    def twoSum(self, nums, target):
        arr = []
        for i in range(len(nums)):
            j = len(nums) -1
            while j > i:
                value = nums[i] + nums[j]
                arr.append([value,i,j])
                j-=1

        for i in arr:
            if i[0] == target:
                return [i[1],i[2]]
        
        
#두번째 시도
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = target - nums[i]
            j = i+1
            while j < len(nums):
                if temp == nums[j]:
                    return [i,j]
                j+=1
        
