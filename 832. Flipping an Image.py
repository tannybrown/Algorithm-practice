class Solution(object):
    def flipAndInvertImage(self, image):
        ans = []
        for i in image:
            arr = []
            for j in i:
                arr.append(1 if j == 0 else 0)
            ans.append(arr[::-1])
        return ans
