import sys, heapq
input = sys.stdin.readline

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b: parents[b] = a
    else: parents[a] = b

V,E = map(int, input().split())
heap = []
parents = [i for i in range(V+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

result = []
while heap:
    if len(result) == V: break
    weight, src, dst = heapq.heappop(heap)
    if find(src) != find(dst):
        union(src, dst)
        result.append(weight)

print(sum(result))