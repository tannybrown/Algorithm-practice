def solution(people, limit):
    people.sort()
    i = 0
    answer = 0
    l = len(people)
    while people :
        if l -1 == i :
            return answer + 1
        if l - 2 == i :
            if people[i] + people[i+1] <= limit:
                return answer + 1
            else :
                return answer + 2
        if people[i] + people[-1] <= limit :
            i += 1
            people.pop()
            l -= 1
            answer += 1
        else :
            answer += 1
            l -= 1
            people.pop()
        # print(people)
        # print(answer)
    return answer
            
print(solution([70, 50, 80, 50],100))
