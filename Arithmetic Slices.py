class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        # make difference array
        arr=[]
        for i in range(len(nums)-1):
            arr.append(nums[i] - nums[i+1])
        answer = 0
        temp = 1
                
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                temp +=1;
            else :
                if temp == 1:
                    temp = 1
                else :
                    answer += (temp * (temp-1))/2
                    temp = 1
        answer += (temp * (temp-1))/2
        return int(answer)
