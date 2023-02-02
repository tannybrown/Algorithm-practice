num = int(input())
#결과 담을 배열
result = []
#수열
sequence = 1
#스택
stack = []
#입력값
target = []
for _ in range(num) :
    target.append(int(input()))

index = 0
tar = target[0]

check = 0
while 1 :
    if tar > sequence : 
        stack.append(sequence)
        sequence +=1
        result.append("+")
    elif tar == sequence :
        sequence += 1
        result.append("+")
        result.append("-")
        if index == num -1 : break
        else : index += 1
        tar = target[index]
    else : 
        if stack[-1] == tar :
            result.append("-")
            stack.pop()
            if index == num -1 : break
            else : index += 1
            tar = target[index]    
        else :
            check = 1
            break
  
if not check :
    for item in result :
        print(item)
else : print("NO")
