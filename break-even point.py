n = input()
arr1 = n.split(" ")
map_object = map(int, arr1)

arr = list(map_object)
answer = 0
if arr[2] - arr[1] <= 0:
    print(-1)
else : 
    answer = arr[0] // (arr[2]-arr[1])
    print(answer + 1)
