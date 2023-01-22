import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
resident = list(map(int, input().split()))

resident.insert(0,0)


adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

dp = [[0,0] for _ in range(n+1)]

for _ in range(n-1):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)


def dfs(now):
    dp[now][0] = resident[now]  #그 마을을 우수마을로 선정하는 경우
    dp[now][1] = 0              #그 마을을 우수마을로 선정하지 않는 경우
    visited[now] = True
    
    for nxt in adj[now]:
        if not visited[nxt]:
            dfs(nxt)

            dp[now][0] += dp[nxt][1]
            dp[now][1] += max(dp[nxt][0],dp[nxt][1])
            
dfs(1)
print(max(dp[1][0], dp[1][1]))
