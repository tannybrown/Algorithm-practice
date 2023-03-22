import math
def solution(progresses, speeds):
    # 우선은 각 progress마다 speeds를 고려해서 100이상이 되기위해 얼마가 필요한지 계산.
    # 이후에 첫번째 요소보다 뒤의 요소가 작거나 같다면, 같이 배포해야하니까 카운트를 올린다.
    # 더 큰 경우에는 카운트를 초기화하고 다시 뒤를 세자.
    # 두번의 반복문을 돌기보다 한번에 원콤으로 끝내도록 짜보자.
    stack = 0
    cur = 0
    ans = []
    
    for i in range(len(progresses)) :
        temp = (100 - progresses[i])//speeds[i]
        if ((100 - progresses[i]) % speeds[i]) :
            temp+= 1
        if not stack :
            cur = temp
            stack += 1
        elif temp > cur :
            ans.append(stack)
            stack = 1
            cur = temp
        else :
            stack += 1
    ans.append(stack)
        
    return ans
