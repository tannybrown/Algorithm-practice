def solution(n):
    count = 1
    while n != 1 :
        if n % 2 :
            count += 1
        n //= 2
    return count
