from collections import deque

n = int(input())
queue = deque(list(range(1,n+1)))

while n != 1 :
    queue.popleft()
    n -= 1
    temp = queue.popleft()
    queue.append(temp)
    

print(queue[0])
