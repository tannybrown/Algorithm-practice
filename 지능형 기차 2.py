#input 담을 배열 선언
arr = []
for i in range(10):
    a = input()
    arr.append(a.split(" "))


max = 0
cnt = 0

#매번 cnt를 계산해서 최대값만 기억
for i in range(10):
    cnt = cnt - int(arr[i][0]) + int(arr[i][1])
    if cnt > max:
        max = cnt

#출력
print(max)
