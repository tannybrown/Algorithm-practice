class Solution(object):
    def countPrefixes(self, words, s):
        count = 0
        check = True
        for i in words:
            if len(i) <= len(s) :
                check = True
                for j in range(len(i)) :
                    if i[j] != s[j]:
                        check = False
                if check == True:
                    count+=1
        return count
