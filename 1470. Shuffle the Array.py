class Solution(object):
    def shuffle(self, nums, n):
        for i in range(n):
            nums.append(nums[i])
            nums.append(nums[n+i])
        return nums[2*n:]
