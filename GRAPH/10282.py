from heapq import heappush, heappop
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    heap = []
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
        
    dist = [sys.maxsize] * (N+1)
    dist[C] = 0
    heappush(heap, [0, C])

    while heap:
        weight, node = heappop(heap)
        if dist[node] < weight:
            continue
        for newNode, _weight in graph[node]:
            new_weight = weight + _weight
            if new_weight < dist[newNode]:
                dist[newNode] = new_weight
                heappush(heap, [new_weight, newNode])

    result = [d for d in dist[1:] if d != sys.maxsize]
    print(len(result), max(result))
