from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(heap, i)

result = []
while heap:
    x = heappop(heap)
    result.append(x)
    for v in graph[x]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heappush(heap, v)

print(*result)