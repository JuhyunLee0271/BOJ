from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
dp = [0] * (N+1)
cost = [0]

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    cost.append(arr[0])
    if arr[1] != 0:
        for j in range(2, len(arr)):
            graph[arr[j]].append(i)
            indegree[i] += 1

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

print(max(dp))