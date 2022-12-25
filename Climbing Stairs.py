class Solution(object):
    def climbStairs(self, n):
        if n == 1 : return 1;
        elif n == 2 : return 2;
        a = 1;
        b = 1;
        t = 0;
        for i in range(1,n):
            t = b
            b = a + b
            a = t

        return b;
