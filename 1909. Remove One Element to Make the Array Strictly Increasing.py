class Solution(object):
    def canBeIncreasing(self, nums):
        #길이가 2면 true
        if len(nums) == 2 :
            return True
        count = 0
        if nums[0]>=nums[1] :
            count+=1
        if len(nums)==3 and nums[0] < nums[1] and nums[1] > nums [2] :
            return True

        for i in range(1,len(nums)-1) :
            if nums[i] >= nums[i+1] :
                if nums[i-1] < nums[i+1] :
                    count += 1
                else :
                    if (len(nums) - 1) < (i + 2) and len(nums) != 3 :
                        count +=1
                    else : 
                        if len(nums) != 3 and nums[i+2] > nums[i]:
                            count += 1
                        else : return False
            if count >= 2 :
                return False
        
        return True
