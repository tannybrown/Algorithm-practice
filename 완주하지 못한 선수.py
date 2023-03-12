def solution(participant, completion):
    dic = {}
    tot = 0
    for part in participant :
        dic[hash(part)] = part
        tot += hash(part)
    for com in completion :
        tot -= hash(com)
    
    return dic[tot]
