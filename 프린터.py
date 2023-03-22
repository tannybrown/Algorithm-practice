def solution(priorities, location):
    # location 을 만져주자.
    # 즉슨, 순서가 바뀌어야 한다면 계산해서 뒤로 보내주는? 방식으로 해보자. location 업데이트?
    
    target = priorities[location]
    ret = 0
    while  1 :
        # max 찾기
        maximum = -1
        indexofmax = -1
        for i in range(len(priorities)) :
            if maximum < priorities[i] :
                maximum = priorities[i]
                indexofmax = i
        # max가 target과 같다면?
        # index가 같은지 확인해보고,
        # index도 같다면 끝.
        # index가 다르다면 중복 경우 이므로 찾은 max기준으로 다시 같은 방식 수행.
        
        if indexofmax == location :
            return ret + 1
        # 여기부턴 이제 틀린경우니까 배열 다시 만들어야함.
        ret += 1
        priorities = priorities[indexofmax+1:] + priorities[:indexofmax]
        # location 재지정
        # max 보다 더 큰 경우
        if location > indexofmax :
            location = location - indexofmax - 1
        # 더 작은 경우
        else :
            location = len(priorities) - indexofmax + location 
            
        
