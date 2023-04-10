# 벽과 자기 자신의 몸과 부딪히면 게임 끝.
# 즉 자신의 몸에 대한 정보를 추적할 수 있어야함.
# 뱀의 몸이 줄어들고 늘어나는 방식이 queue와 같음.
# 즉 queue를 이용할 것.

# 주어진 명령에 맞춰 이동을 하고, 한번의 이동시마다, 자기자신의 몸인지, 벽인지를 체크.
# 아니라면 사과의 유무를 체크한다.
# 와 같은 방식으로 구현해보자.

from collections import deque

# 판 사이즈
N = int(input())

# 사과 위치
apple_count = int(input())
apple = []
for _ in range(apple_count) :
    a,b = input().split(" ")
    apple.append((int(a),int(b)))

dict = {}
# 방향전환
turn_count = int(input())

for _ in range(turn_count) :
    a,b = input().split(" ")
    dict[int(a)] = b

# 입력은 끝이 났다. 이제 뱀의 정보를 넣어보자.
bam = deque([(1,1)])
# 움직이는 방향. 4은 오른쪽, 5는 위, 6은 좌, 7는 아래 (0,1,2,3)
# L 은 1증가, D는 1감소
move = 0
cur_x = 1
cur_y = 1

# 출력할 시간
time =  0

while 1 :
    time += 1

    # print(time)
    # print(bam)
    
    
    # move 부터 체크
    if move < 0 :
        move += 4
    elif move > 3 :
        move -= 4
    
    # print(move)

    if move == 0 :
        cur_y += 1
    elif move == 1 :
        cur_x -= 1
    elif move == 2 :
        cur_y -= 1
    else :
        cur_x += 1

    # print((cur_x,cur_y))

    # size 초과 인지 체크
    if cur_x > N or cur_y > N or cur_x < 1 or cur_y < 1:
        # print("size")
        break
    
    # 몸에 닿았는지 체크
    if (cur_x,cur_y) in bam :
        # print("body")
        break

    # 사과 확인하기
    if (cur_x,cur_y) not in apple :

        bam.popleft()
    else :
        apple.remove((cur_x,cur_y))
    # print(apple)
    # bam 앞으로 이동 완료.
    bam.append((cur_x,cur_y))

    # 방향 전환 체크
    if time in dict :
        if dict[time] =="L" :
            move += 1
        else :
            move -= 1


print(time)
