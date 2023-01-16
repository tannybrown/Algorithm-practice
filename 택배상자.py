def solution(order):
    #하나는 무조건 트럭에 실을 수가 있기때문에 while 전에 처리.
    container = order[0] + 1
    container_length = len(order)
    stack = list(range(1,container - 1))
    answer = 1
    # order를 del 해주기 부담스러워서 역순을 만든후, 하나씩 pop해줄 것.
    order = order[::-1]
    order.pop()
    
    #order가 빈배열이면 탈출.
    while order != [] :
        order_top = order[len(order) - 1]
        #container가 안비었다.
        if container <= container_length :
            #container 에서 트럭으로 !
            if container == order_top :
                order.pop()
                container += 1
                answer += 1
            #stack에는 container보다 작은 값만이 들어감, 즉 container가 order보다 작으면 무조건 stack 에 push
            elif container < order_top :
                stack.append(container)
                container += 1
            #order 가 더 작으면. 이건 스택을 뒤져봐야함.
            else : 
                #스택이 비었음. 즉 더 할게 없음 break
                if stack == [] :
                    break
                #stack이 비어있지 않다면, 스택의 top과 비교, 같으면 pop해주자 ,틀리면 끝임
                elif stack[len(stack) - 1] == order_top :
                    stack.pop()
                    order.pop()
                    answer += 1
                else :
                    break
        #container 가 비었다. 그러면, 스택을 봐야함.
        else :
            if stack == [] :
                break
            elif stack[len(stack)-1] == order_top :
                stack.pop()
                order.pop()
                answer += 1
            else :
                break

    return answer
        
