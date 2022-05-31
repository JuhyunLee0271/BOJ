from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 10**9

# heap based dijkstra
def dijkstra(src, dst):
    heap = []
    dist = [INF] * (N+1)
    dist[src] = 0
    heappush(heap, [0, src]) # [weight, node]
    
    while heap:
        weight, node = heappop(heap)
        if dist[node] < weight:
            continue
        
        for newNode, _weight in graph[node]:
            new_weight = weight + _weight
            if dist[newNode] > new_weight:
                dist[newNode] = new_weight
                heappush(heap, [new_weight, newNode])
    
    return dist[dst]
        
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

print(-1) if path1 >= INF and path2 >= INF else print(min(path1, path2))