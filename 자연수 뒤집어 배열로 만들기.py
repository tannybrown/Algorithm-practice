def solution(n):
    arr =[]
    while n != 0: 
        arr.append(n % 10)
        n //= 10
    return arr
