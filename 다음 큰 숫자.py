def solution(n):
    # n의 2진수 , 1의 개수 체크
    binaryN = bin(n)[2:]
    count = 0
    for i in range(len(binaryN)) :
        if binaryN[i] == '1' :
            count += 1
    nextN = n + 1
    while 1 :
        binaryN = bin(nextN)[2:]
        ncount = 0
        for i in range(len(binaryN)) :
            if binaryN[i] == '1' :
                ncount += 1
        if count == ncount :
            return nextN
        else : 
            nextN += 1

