class Solution(object):
    def largeGroupPositions(self, s) :
        answer = []
        count = 0
        for i in range(len(s)-1) :
            if s[i] == s[i+1] :
                count+=1
            else : 
                if count >= 2 :
                    answer.append([i-count,i])
                count = 0
        if count >= 2 :
            answer.append([len(s)-1 -count,len(s)-1])
        return answer
