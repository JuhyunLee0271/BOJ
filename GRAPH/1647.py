import sys, heapq
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return parent[a]
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(0, N+1)]
heap = []
for _ in range(M):
    a,b,c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

result = []
while heap and len(result) < N-2:
    dist, src, dst = heapq.heappop(heap)
    if find(src) != find(dst):
        union(src, dst)
        result.append(dist)
print(sum(result))
