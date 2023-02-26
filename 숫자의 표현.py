def solution(n):
    answer = 0
    startNum = 1
    val = 1
    total = 0
    while startNum <= n :
        total += val
        if total == n :
            answer += 1
            startNum += 1
            val = startNum
            total = 0
            continue
        elif total > n :
            startNum += 1
            val = startNum
            total = 0
            continue
        val += 1
        
    return answer
        
        
