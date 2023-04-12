import sys

n = int(input())
arr = []

for _ in range(n) :
  start, end = sys.stdin.readline().split()
  arr.append([int(start),int(end)])
  

arr.sort(key=lambda x: (x[1], x[0]))

cur = arr[0]
ans = 1
for item in arr[1:] :
  if cur[1] <= item[0] :
    cur = item
    ans += 1
  

print(ans)
