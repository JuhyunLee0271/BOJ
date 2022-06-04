from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def calc_origin_dist():
    origin_dist = [10**9] * (N+1)
    heap = []
    heappush(heap, [0, 1])

    while heap:
        weight, node = heappop(heap)
        if origin_dist[node] < weight:
            continue
        for _weight, newNode in graph[node]:
            new_weight = weight + _weight
            if new_weight < origin_dist[newNode]:
                origin_dist[newNode] = new_weight
                heappush(heap, [new_weight, newNode])
    
    return origin_dist

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b]) # [cost, dst]
    graph[b].append([c, a])

origin_dist = calc_origin_dist()
dist = [10**9] * (N+1)
heap = []
start, cnt = 1, 0 
heappush(heap, [0, start])
dist[start] = 0
answer = []

while heap:
    if cnt == N-1:
        break
    weight, node = heappop(heap)
    if weight > dist[node]:
        continue
    for _weight, newNode in graph[node]:
        new_weight = weight + _weight
        if new_weight < dist[newNode] and new_weight <= origin_dist[newNode]:
            dist[newNode] = new_weight
            heappush(heap, [new_weight, newNode])
            answer.append([node, newNode])
            cnt += 1

print(len(answer))
for src, dst in answer:
    print(src, dst)
