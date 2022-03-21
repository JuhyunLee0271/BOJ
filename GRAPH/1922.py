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
    elif a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b

N = int(input())
M = int(input())
parents = [i for i in range(N+1)]
heap = []
for _ in range(M):
    a,b,c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

result = []

while heap and len(result) < N:
    c, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a,b)
    result.append(c)

print(sum(result))




    
