from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])    
    graph[b].append([a, c])
    
distance = [sys.maxsize] * (N+1)
start, end = 1, N
distance[start] = 0
heap = []
heappush(heap, [1, 0]) # [node, weight]

while heap:
    node, weight = heappop(heap)
    if distance[node] < weight:
        continue
    for newNode, _weight in graph[node]:
        newWeight = weight + _weight
        if newWeight < distance[newNode]:
            distance[newNode] = newWeight
            heappush(heap, [newNode, newWeight])

print(distance[end])