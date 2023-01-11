class Solution(object):
    def isPalindrome(self, x):
        if x < 0 : return False
        arr = []
        while x >= 10 :
            arr.append(x%10)
            x = x // 10
        arr.append(x%10)
        x = x // 10

        print(arr)
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - 1-i]:
                return False
        
        return True
