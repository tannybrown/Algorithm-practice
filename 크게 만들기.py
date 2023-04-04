a,b = map(int,input().split(' '))
number = list(input())

answer = []

cnt = b
for num in number :
    while answer and cnt >0 and answer[-1] <num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:a-b]))
