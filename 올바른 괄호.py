def solution(s):
    stack = 0
    for item in s :
        if item == "(" :
            stack += 1
        elif item == ")" :
            stack -= 1
        if stack < 0 :
            return False
    if stack == 0:
        return True
    else :
        return False
