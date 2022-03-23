from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
start, end = map(int, input().split())

graph = [[]*(N+1) for _ in range(N+1)]

M = int(input())

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(start)
dist = [-1]*(N+1)
dist[start] = 0

while q:
    x = q.popleft()
    for v in graph[x]:
        if dist[v] == -1:
            dist[v] = dist[x] + 1
            q.append(v)

print(dist[end])
