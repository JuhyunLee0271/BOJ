from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
cost = [0]
dp = [0] * (N+1)
for i in range(N):
    arr = list(map(int, input().split()))[:-1]
    cost.append(arr[0])
    if len(arr) > 1:
        for j in range(1, len(arr)):
            graph[arr[j]].append(i+1)
            indegree[i+1] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = cost[i]

while q:
    x = q.popleft()
    for v in graph[x]:
        indegree[v] -= 1
        dp[v] = max(dp[v], dp[x] + cost[v])
        if indegree[v] == 0:
            q.append(v)

for e in dp[1:]:
    print(e)

