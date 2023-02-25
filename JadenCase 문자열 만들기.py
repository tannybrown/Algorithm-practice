def solution(s):
    s1 = s.split(" ")
    answer = []
    for i in s1 : 
        i = i.lower()
        i = i.capitalize()
        answer.append(i)
    a = " ".join(answer)
    return a
