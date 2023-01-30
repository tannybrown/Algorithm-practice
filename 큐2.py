from sys import stdin
iternum = int(input())
data = [stdin.readline().strip() for i in range(iternum)]
queue = []
check = 0
size = 0

for command2 in data :
    command = command2.split()
    if command[0] == "push" :
        queue.append(command[1])
        size += 1
    elif command[0] == "pop": 
        if not size :
            print(-1)
            queue = []
            check = 0
        else :
            print(queue[check])
            check+=1
            size -=1
    elif command[0] == "size" :
        print(size)
    elif command[0] == "empty":
        if not size :
            print(1)
            check = 0
            queue = []
        else :
            print(0)
    elif command[0] == "front":
        if not size :
            print(-1)
            check = 0
            queue = []
        else :
            print(queue[check])
    elif command[0] == "back" :
        if not size :
            print(-1)
            check = 0
            queue = []
        else : 
            print(queue[-1])  
