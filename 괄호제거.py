from itertools import combinations

expression = input()
arr = []
index = []
result=[]
#괄호를 배열에 담기
for i in range(len(expression)):
    if expression[i] == '(':
        arr.append(i)
    elif expression[i] == ')':
        index.append([arr.pop(), i])

#괄호 제거와 result에 append
for i in range(1, len(index)+1):
    combs = list(combinations(index, i))
    for comb in combs:
        check = []
        answer = []
        for com in comb:
            check.append(com[0]); check.append(com[1])

        for j in range(len(expression)):
            if j in check:
                continue
            else:
                answer.append(expression[j])
        result.append(''.join(answer))
# 중복제거
result = set(result)
# 사전순 sort
result = sorted(list(result))
# 출력
for res in result:
    print(res)
