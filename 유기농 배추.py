import sys

sys.setrecursionlimit(10**9)


num = input()
for _ in range(int(num)) :

    arr = input().split(" ")
    matrix = []
    x = int(arr[0])
    y = int(arr[1])
    for i in range(x) :
        matrix.append([])
        for j in range(y) :
            matrix[i].append(0)

    
    
    for i in range(int(arr[2])) :
        a = input().split(" ")
        matrix[int(a[0])][int(a[1])] = 1
        
    def check(x1,y1) :
        if matrix[x1][y1] == 1 :
            matrix[x1][y1] = 2
            if y1 + 1 < y :
                check(x1,y1+1)
            if y1 -1 >= 0 :
                check(x1,y1-1)
            if x1 + 1  < x :   
                check(x1+1,y1)
            if x1 - 1 >= 0:
                check(x1-1,y1)
            
    
    count = 0
    for i in range(x):
        for j in range(y) :
            if matrix[i][j] == 1 :
                count+=1
                matrix[i][j] = 2    
                if j-1 >= 0 :            
                    check(i,j-1)
                if i - 1 >= 0 :
                    check(i-1,j)
                if i + 1 < x :
                    check(i+1,j)
                if j + 1 < y :
                    check(i,j+1)
                

    print(count)
            

  
