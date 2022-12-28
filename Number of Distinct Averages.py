class Solution(object):
    def distinctAverages(self, arr):
        arr.sort()
        answer=[]
        for i in range(len(arr)//2):
            answer.append(arr[i]+arr[len(arr)-i-1])

        answer= set(answer)

        return len(answer)
