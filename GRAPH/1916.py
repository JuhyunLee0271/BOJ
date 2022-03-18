import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] * (N+1) for i in range(N+1)]
heap = []
for _ in range(M):
    # src, dst, weight
    a,b,c = map(int, input().split())
    graph[a].append((c,b))

start, end = map(int, input().split())
result = [INF] * (N+1)
result[start]  = 0

heapq.heappush(heap, (0, start))

while heap:
    weight, node = heapq.heappop(heap)
    if result[node] < weight:
        continue
    for _weight, nextNode in graph[node]:
        new_weight = weight + _weight
        if new_weight < result[nextNode]:
            result[nextNode] = new_weight
            heapq.heappush(heap, (new_weight, nextNode))

print(result[end])


