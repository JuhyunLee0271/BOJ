import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
heap = []
dist = [sys.maxsize] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
dist[start] = 0
heappush(heap, (0, start, [start]))

while heap:
    weight, node, path = heappop(heap)
    if weight > dist[node]:
        continue
    if node == end:
        print(dist[end])
        print(len(path))
        print(*path)
    visited[node] = True
    for nextNode, _weight in graph[node]:
        new_weight = weight + _weight
        if new_weight < dist[nextNode] and not visited[nextNode]:
            dist[nextNode] = new_weight
            heappush(heap, (new_weight, nextNode, path+[nextNode]))


