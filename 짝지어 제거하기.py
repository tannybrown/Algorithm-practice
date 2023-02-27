def solution(s):
    stack = []
    for item in s :
        if stack == [] :
            stack.append(item)
        else :
            if stack[-1] == item :
                stack.pop()
            else :
                stack.append(item)
    if stack == [] :
        return 1
    return 0
