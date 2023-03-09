def solution(s):
    ans = 0
    stack = []
    l = len(s)
    #회전 하나씩 보기
    for i in range(l) :
        flag = 0
        stack = []
        n = 0
        j = i
        while l > n :
            # print(stack)
            # print(s[i])
            if s[j] == "[" :
                stack.append(1)
            elif s[j] == "{" :
                stack.append(2)
            elif s[j] == "(" :
                stack.append(3)
            else :
                if s[j] == "]" :
                    if not stack :
                        flag = -1
                        break
                    elif stack[-1] == 1 :
                        stack.pop()
                    else :
                        flag = -1
                        break
                elif s[j] == "}" :
                    if not stack :
                        flag = -1
                        break
                    elif stack[-1] == 2 :
                        stack.pop()
                    else :
                        flag = -1
                        break
                elif s[j] == ")" :
                    if not stack :
                        flag = -1
                        break
                    elif stack[-1] == 3 :
                        stack.pop()
                    else :
                        flag = -1
                        break
                        
                
            n += 1
            j += 1
            if j == l :
                j = 0
        if flag == -1 or stack :
            pass
        else : 
            ans += 1
    return ans

# print(solution("}]()[{"))
