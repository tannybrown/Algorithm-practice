import math

def solution(arr):
    def lcm(a, b):
        return a * b // math.gcd(a, b)
    arr.sort()
    ans = arr[-1]
    for i in range(len(arr)-1) :
        ans = lcm(ans,arr[i])
    
    return ans
