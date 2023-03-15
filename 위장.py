# 일단 카테고리 별로 겹치면 안됌.
# 같은 카테고리일 경우 겹치지 않도록.
# 흠..카테고리수, 카테고리별 개수를 새기만 하면 될듯?
# 카테고리수를 알면, 1개씩 있는 경우의 조합수를 계산할 수 있음.
# 그리고 각각에 카테고리별 개수를 곱해주면 경우의 수를 계산할 수 있을 것.
# 근데 곱해주려면 각각을 기억해야하니까, hash를 통해서 해보는게 좋을듯?!
# 언제나 문자열 비교는 heavy하니 해시를 사용할 수 있다면 해보자.

def solution(clothes):
    category = []
    dic = {}
    for c in clothes :
        if hash(c[1]) in category :
            
            dic[hash(c[1])] += 1
        else :    
            category.append(hash(c[1]))
            dic[hash(c[1])] = 1
    
    ## 여기서 이제 , 경우의 수가 (안입는경우 + 옷장가짓수) 이므로 +1 해서 계산해때리고 마지막에 전부안입는걸 빼주면 된다.
    answer = 1
    for item in category :
        answer *= dic[item] + 1
    
    return answer - 1
            
