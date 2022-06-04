from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    elif a < b: parent[b] = a
    else: parent[a] = b

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
sex = [0] + list(input().rstrip().split())
heap = []

for _ in range(M):
    u, v, d = map(int, input().split())
    heappush(heap, [d, u, v])

cnt = 0
answer = []
while heap:
    if cnt == N - 1:
        break
    weight, src, dst = heappop(heap)
    if find(src) != find(dst) and sex[src] != sex[dst]:
        union(src, dst)
        answer.append(weight)
        cnt += 1

print(sum(answer)) if len(answer) == N-1 else print(-1)
        
        