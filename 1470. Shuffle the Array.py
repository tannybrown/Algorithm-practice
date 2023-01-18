class Solution(object):
    def shuffle(self, nums, n):
        for i in range(n):
            nums.append(nums[i])
            nums.append(nums[n+i])
        return nums[2*n:]
    
# 다른 방법
class Solution(object):
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
        return ans
