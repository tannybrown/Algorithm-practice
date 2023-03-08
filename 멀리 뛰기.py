import operator as op
from functools import reduce

def solution(n):
    one = n
    two = 0
    ans = 0
    if n == 1 :
        return 1

    def nCr(n, r):
        # if n < 1 or r < 0 or n < r:
        #     raise ValueError
        r = min(r, n-r)
        numerator = reduce(op.mul, range(n, n-r, -1), 1)
        denominator = reduce(op.mul, range(1, r+1), 1)
        return numerator // denominator

    while 1 :
        if one == 0 :
            return (ans + 1)% 1234567
        elif one == 1 :
            return (ans + two + 1)% 1234567
        else :
            ans += nCr(one+two,one)
            
            one -= 2
            two += 1
