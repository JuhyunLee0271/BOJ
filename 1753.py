import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

heap = []
graph = [[] for _ in range(V+1)]
result = [INF for _ in range(V+1)]
result[K] = 0

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))

heapq.heappush(heap, (0, K))

while heap:
    weight, now = heapq.heappop(heap)
    if result[now] < weight:
        continue
    for _weight, next_node in graph[now]:
        _weight += weight
        if _weight < result[next_node]:
            result[next_node] = _weight
            heapq.heappush(heap, (_weight, next_node))

for e in result[1:]:
    print("INF" if e == INF else e)
