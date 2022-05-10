from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(src, dst):
    dist = [sys.maxsize] * (N+1)
    dist[src] = 0
    heap = []
    heappush(heap, [0, src])
    
    while heap:
        weight, node = heappop(heap)
        if dist[node] < weight:
            continue
        for newNode, _weight in graph[node]:
            new_weight = weight + _weight
            if new_weight < dist[newNode]:
                dist[newNode] = new_weight
                heappush(heap, [new_weight, newNode])
    
    return dist[dst]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
heap = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

answer = 0
for node in list(set(i for i in range(1, N+1)) - {X}):
    a, b = dijkstra(node, X), dijkstra(X, node)
    answer = max(answer, a + b)

print(answer)