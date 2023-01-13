arr = []

arr.append(input())
arr.append(input())
arr.append(input())

for i in arr:
    count=0
    ut = i.split(" ")
    for j in ut:
        if j == "1":
            count+=1
    if count == 0:
        print("D")
    elif count == 1:
        print("C")
    elif count == 2:
        print("B")
    elif count == 3:
        print("A")
    else : print("E")
