from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append((1, 0))
visited[1] = True
result = 0

while q:
    node, dist = q.popleft()
    if dist == 2:
        break
    for v in graph[node]:
        if not visited[v]:
            visited[v] = True
            q.append((v, dist + 1))
            result += 1

print(result)

