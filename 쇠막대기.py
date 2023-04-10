#굳이 스택구조를 쓸필요가 있나? 싶어서
# 일단은 변수로 해보자.
# 만들것은, top(스택의 top을 의미) , 그리고 현재 오픈된 것의 수 steel 이라고 하자.
# 또.. 잘린것의 수는 answer 로 두자.

#우선 입력부터 받기.
arr = input()
top = arr[0]
steel = 0
answer = 0

if top == "(" :
    steel += 1

for item in arr[1:] :
    if item == "(" :
        steel += 1
        top = "("
    else :
        if top == "(" :
            steel -= 1
            answer += steel
            top = ")"
        else :
            answer += 1
            steel -= 1
            top = ")"

print(answer)
