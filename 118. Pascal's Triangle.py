class Solution(object):
    def generate(self, numRows):
        if numRows == 1 :
            return [[1]]
        if numRows == 2 :
            return [[1],[1,1]]
        answer = [[1],[1,1]]

        for _ in range(numRows-2) :
            count = len(answer)
            past = answer[count - 1]
            arr = []
            for iter in range(count+1) :
                if iter == 0 or iter == count :
                    arr.append(1)
                else :
                    arr.append(past[iter] + past[iter-1])
            answer.append(arr)
        return answer 
