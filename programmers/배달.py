from heapq import heappush, heappop
import sys

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    heap = []
    dist = [sys.maxsize] * (N+1)
    dist[1] = 0
    
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    # [weight, node]
    heappush(heap, [0, 1])
    while heap:
        weight, node = heappop(heap)
        if dist[node] < weight:
            continue
        for newNode, _weight in graph[node]:
            new_weight = weight + _weight
            if new_weight < dist[newNode]:
                dist[newNode] = new_weight
                heappush(heap, [new_weight, newNode])
    return len([d for d in dist if d <= K])