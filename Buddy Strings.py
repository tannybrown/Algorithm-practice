class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) == 1 or len(s) != len(goal):
            return False

        if set(s) == set(goal) and len(set(s)) == 1 :
            return True
        
        arr1 = []
        arr2 = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                arr1.append([s[i],goal[i]])
            else :
                arr2.append(s[i])

        if len(s) == len(arr2) and len(set(arr2)) != len(arr2):
            return True

        if len(arr1) != 2 :
            return False

        if arr1[0][0] == arr1[1][1] and arr1[0][1] == arr1[1][0]:
            return True
