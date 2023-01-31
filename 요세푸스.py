input = input().split(" ")
n,k = int(input[0]),int(input[1])

circle = list(range(1,n+1))
result = []
old = 0

while circle != [] :
    leng = len(circle) 
    if leng >= k :
        if leng >= old + k :
            result.append(circle.pop(old+k-1))
            old = old + k - 1
            
        else :
            circle = circle[old:] + circle[:old]
            old = 0
    else :
        temp_k = k % leng
        if leng >= old + temp_k :
            result.append(circle.pop(old+temp_k-1))
            old = old + temp_k - 1 
            if old == -1 : old = 0
        else :
            circle = circle[old:] + circle[:old]
            old = 0


str1 = "<"    
for i in range(len(result)) :
    if i != len(result) -1 :
        str1 += (str(result[i]) +', ')
    else : 
        str1 += str(result[i])
print(str1+">") 
