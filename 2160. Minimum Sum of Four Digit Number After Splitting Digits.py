class Solution(object):
    def minimumSum(self, num):
        num = str(num)
        map_object = map(int, num)
        num = list(map_object)
        num.sort()
        return int(str(num[0]) + str(num[2]))+int(str(num[1]) + str(num[3]))
